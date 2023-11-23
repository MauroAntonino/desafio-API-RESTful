from restapi.user.entities.interfaces.user_repository_interface import UserRepositoryInterface
from restapi.user.entities.objects.user import User
from restapi.user.entities.objects.movie import Movie
import logging
from os import getenv, path, makedirs
import uuid
import re
logger = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')
from typing import List

def default_create_user(user: User):
    user.user_id = uuid.uuid4().int
    user.image_url = user.user_id
    user.is_confirmed = False
    return user

def default_update_user(user: User):
    user.user_id = uuid.uuid4().int
    user.image_url = user.user_id
    user.is_confirmed = False
    return user

def check_user(email, password):
    return True

class UserRepositoryAdapterHelper(UserRepositoryInterface):

    def __init__(
        self,  
        check_user=check_user, 
        update_user=default_update_user, 
        save_image=None, 
        get_movies=None, 
        get_best_movies=None, 
        email_is_valid=None, 
        is_email_checked=None,
        create_user=default_create_user,
    ):
        self.create_user = create_user
        self.update_user = update_user
        self.check_user = check_user
    
    def validate_user(self, user: User):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not re.fullmatch(regex, user.email)):
            raise Exception("Invalid Email")

        if len(user.password) < 8:
            raise Exception("Make sure your password is at lest 8 letters")

        if (type(user.name) == str) and (len(user.name) < 5):
            raise Exception("Make sure your user name is at lest 5 letters")
    
    def validate_update_user(self, user: User):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if user.email != None:
            if(not re.fullmatch(regex, user.email)):
                raise Exception("Invalid Email")
        
        if user.password != None:
            if len(user.password) < 8:
                raise Exception("Make sure your password is at lest 8 letters")
        
        if user.name != None:
            if (type(user.name) == str) and (len(user.name) < 5):
                raise Exception("Make sure your user name is at lest 5 letters")
      

    def create_user(self, user: User) -> User:
        pass
    
    def check_user(self, email, password) -> bool:
        pass

    def update_user(self, user: User) -> User:
        pass
    
    def save_image(self, image, user: User):
        pass

    def get_movies(self, page_size, page, search, order) -> List[Movie]:
        pass
    
    def get_best_movies(self, page_size, page, search, order) -> List[Movie]:
        pass
    
    def email_is_valid(self, email):
        pass
    
    def is_email_checked(self, email) -> bool:
        pass