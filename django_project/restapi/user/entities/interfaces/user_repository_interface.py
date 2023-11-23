import abc
from restapi.user.entities.objects.user import User
from restapi.user.entities.objects.movie import Movie
from typing import List

class UserRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def check_user(self, email, password) -> bool:
        """Check User"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def create_user(self, user: User) -> User:
        """Create User"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def validate_user(self, user: User):
        """Validate User"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def update_user(self, user: User) -> User:
        """Update User"""
        raise NotImplementedError
    
    def validate_update_user(self, user: User) -> User:
        """Validate Update User"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def save_image(self, image):
        """Save User Image"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_movies(self, page_size, page, search, order) -> List[Movie]:
        """Get Best Movies"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def is_email_checked(self, email) -> bool:
        """Get If Email Is Checked"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_best_movies(self, page_size, page, search, order):
        """Get Best Movies"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def email_is_valid(self, email):
        """Update is_valid Field"""
        raise NotImplementedError
    
    