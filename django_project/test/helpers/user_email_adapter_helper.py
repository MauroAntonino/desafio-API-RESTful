from restapi.user.entities.interfaces.user_email_interface import UserEmailInterface
from itsdangerous import URLSafeTimedSerializer
from os import getenv

def generate_token(email):
    serializer = URLSafeTimedSerializer("string")
    return serializer.dumps(email, salt="string")

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer("string")
    try:
        email = serializer.loads(
            token, salt="string", max_age=expiration
        )
        return email
    except Exception:
        return False

class UserEmailAdapterHelper(UserEmailInterface):

    def __init__(
            self,
            generate_token=generate_token,
            confirm_token=confirm_token,
            email_send_token=None

        ):
        self.generate_token=generate_token
        self.confirm_token=confirm_token
    
    def generate_token(self, email):
        pass
    
    def confirm_token(self, token, expiration=3600):
        pass

    def email_send_token(self, email, token):
        pass