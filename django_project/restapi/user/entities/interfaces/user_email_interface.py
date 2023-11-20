import abc
from restapi.user.entities.objects.user import User
from typing import List

class UserEmailInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_token(self, email):
        """Generate Token"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def confirm_token(self, token, expiration):
        """Confirm Token"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def send_email(email, token):
        """Send Email"""
        raise NotImplementedError