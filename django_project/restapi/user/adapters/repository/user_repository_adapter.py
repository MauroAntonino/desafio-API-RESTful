from restapi.user.entities.interfaces.user_repository_interface import UserRepositoryInterface
from restapi.user.entities.objects.user import User
from restapi.user.entities.objects.movie import Movie
import uuid
import hashlib
import json
import logging
from os import getenv, path, makedirs
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import re
logger = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')

class UserRepositoryAdapter(UserRepositoryInterface):

    def __init__(self, database) -> None:
        self.db = database()
    
    def validate_user(self, user: User):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not re.fullmatch(regex, user.email)):
            raise Exception("Invalid Email")
        
        if len(user.password) < 8:
            raise Exception("Make sure your password is at lest 8 letters")
        
        if (type(user.name) == str) and (len(user.name) < 5):
            raise Exception("Make sure your user name is at lest 5 letters")
      

    def create_user(self, user: User) -> User:
        db = self.db.connect()
        cursor = db.cursor()
        id = uuid.uuid4().int
        m = hashlib.sha256()
        m.update(json.dumps(user.password).encode("utf-8"))
        password = str(m.hexdigest())
        email = user.email
        user.image_url = id
        image_url = user.image_url
        
        query = ("INSERT INTO User ( name, password, email, id, image_url, is_confirmed )"
                 "VALUES( '{name}', '{password}', '{email}', '{id}', '{image_url}', '{is_confirmed}');".format(
                    password=password, 
                    email=email,
                    id=id,
                    name=user.name,
                    image_url=image_url,
                    is_confirmed=0
                ))
        try:
            cursor.execute(query)
        except Exception as ex:
            logger.error(ex)
            raise Exception('User already exists')
        db.commit()
        cursor.close()
        db.close()
        user.user_id = id
        user.is_confirmed = False
        return user
    
    def check_user(self, email, password) -> bool:
        db = self.db.connect()
        cursor = db.cursor()
        query = ("SELECT password, id FROM User WHERE email = '{email}'".format(email=email))

        cursor.execute(query)
        response = [item for item in cursor]
        cursor.close()
        db.close()
        try:
            user_id = response[0][1]
            password_code = response[0][0]
        except:
            raise(Exception("user not found"))
        m = hashlib.sha256()
        m.update(json.dumps(password).encode("utf-8"))
        password = str(m.hexdigest())
        if (password_code == password):
            return True
        else:
            return False

    def update_user(self, user: User) -> User:
        db = self.db.connect()
        cursor = db.cursor()
        query = None
        if (user.name != None):
            query = ("UPDATE User SET name = '{name}' WHERE email = '{email}'".format(email=user.email, name=user.name))
        try:
            cursor.execute(query)
        except:
            raise Exception("User does not exist")
        
        if (user.password != None):
            m = hashlib.sha256()
            m.update(json.dumps(user.password).encode("utf-8"))
            password = str(m.hexdigest())
            query = ("UPDATE User SET password = '{password}' WHERE email = '{email}'".format(email=user.email, password=password))
        try:
            cursor.execute(query)
        except:
            raise Exception("User does not exist")
        
        query = ("SELECT id, image_url, is_confirmed FROM User WHERE email = '{email}'".format(email=user.email))
        cursor.execute(query)
        response = [item for item in cursor]
        id, image_url, is_confirmed = response[0][0], response[0][1], response[0][2]
        user.user_id = id
        user.image_url = image_url
        user.is_confirmed = is_confirmed
        
        db.commit()
        cursor.close()
        db.close()
        return user
    
    def save_image(self, image, user: User):
        if image != None:
            image.name = str(user.user_id)
            fs = FileSystemStorage(location=settings.STATIC_ROOT)
            filename = fs.save(image.name, image)
            logger.info(filename)
        return "success"

    def get_movies(self, page_size, page, search, order):
        db = self.db.connect()
        cursor = db.cursor()
        if search == None:
            query = ("SELECT name, rating, year FROM Movie "
                    "LIMIT {page}, {page_size};".format(page_size=page_size, page=page, search=search, order=order))
        if search != None:
            query = ("SELECT name, rating, year FROM Movie "
                    "WHERE name LIKE '%{search}%' "
                    "LIMIT {page}, {page_size};".format(page_size=page_size, page=page, search=search, order=order))
        cursor.execute(query)
        response = [item for item in cursor]
        cursor.close()
        db.close()
        try:
            movie_list = []
            for item in response:
                name, rating, year = item[0], item[1], item[2]
                movie = Movie(
                                name=name, 
                                rating=rating, 
                                year=year
                            )
                movie_list.append(movie)
            if order == "year":
                movie_list.sort(key=lambda x: x.year, reverse=True)
            if order == "rating":
                movie_list.sort(key=lambda x: x.rating, reverse=True)
        except Exception as ex:
            print(ex)
            raise(Exception("Faiel getting movies"))
        return movie_list
    
    def get_best_movies(self, page_size, page, search, order):
        db = self.db.connect()
        cursor = db.cursor()
        if search == None:
            query = ("SELECT name, rating, year FROM BestMovie "
                    "LIMIT {page}, {page_size};".format(page_size=page_size, page=page, search=search, order=order))
        if search != None:
            query = ("SELECT name, rating, year FROM BestMovie "
                    "WHERE name LIKE '%{search}%' "
                    "LIMIT {page}, {page_size};".format(page_size=page_size, page=page, search=search, order=order))
        cursor.execute(query)
        response = [item for item in cursor]
        cursor.close()
        db.close()
        try:
            movie_list = []
            for item in response:
                name, rating, year = item[0], item[1], item[2]
                movie = Movie(
                                name=name, 
                                rating=rating, 
                                year=year
                            )
                movie_list.append(movie)
            if order == "year":
                movie_list.sort(key=lambda x: x.year, reverse=True)
            if order == "rating":
                movie_list.sort(key=lambda x: x.rating, reverse=True)
        except Exception as ex:
            print(ex)
            raise(Exception("Faiel getting movies"))
        return movie_list
    
    def email_is_valid(self, email):
        db = self.db.connect()
        cursor = db.cursor()
        query = ("UPDATE User SET is_confirmed = '{is_confirmed}' WHERE email = '{email}'".format(email=email, is_confirmed=1))
        try:
            cursor.execute(query)
        except:
            raise Exception("User does not exist")
        
        db.commit()
        cursor.close()
        db.close()
    
    def is_email_checked(self, email):
        db = self.db.connect()
        cursor = db.cursor()
        
        query = ("SELECT is_confirmed FROM User WHERE email = '{email}'".format(email=email))
        cursor.execute(query)
        response = [item for item in cursor]
        is_confirmed = response[0][0]
        
        db.commit()
        cursor.close()
        db.close()
        if int(is_confirmed) == 0:
            return False
        else:
            return True