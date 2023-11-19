import abc
from restapi.user.entities.objects.user import User
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
    def update_user(self, user: User, image) -> User:
        """Update User"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def save_image(self, image):
        """Save User Image"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_image(self, image):
        """Save User Image"""
        raise NotImplementedError