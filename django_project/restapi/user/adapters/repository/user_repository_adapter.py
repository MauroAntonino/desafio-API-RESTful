from restapi.user.entities.interfaces.user_repository_interface import UserRepositoryInterface
from restapi.user.entities.objects.user import User
import uuid
import hashlib
import json
import logging
from os import getenv, path
import re
logger = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'uploads')

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
        extension = ".jpeg"
        user.image_url = "/{id}/{image_name}{extension}".format(id=id, image_name=user.name, extension=extension)
        image_url = user.image_url
        
        query = ("INSERT INTO User ( name, password, email, id, image_url )"
                 "VALUES( '{name}', '{password}', '{email}', '{id}', '{image_url}');".format(
                    password=password, 
                    email=email,
                    id=id,
                    name=user.name,
                    image_url=image_url
                ))
        try:
            cursor.execute(query)
        except:
            raise Exception('User already exists')
        db.commit()
        cursor.close()
        db.close()
        user.user_id = id
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
        logger.debug(password_code)
        m = hashlib.sha256()
        m.update(json.dumps(password).encode("utf-8"))
        password = str(m.hexdigest())
        logger.debug(password)
        if (password_code == password):
            return True
        else:
            return False

    def update_user(self, email, name, password) -> User:
        pass
    
    def save_image(self, image):
        pass

    def get_image(self, image):
        pass