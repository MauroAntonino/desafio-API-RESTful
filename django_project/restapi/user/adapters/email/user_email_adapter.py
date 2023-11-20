from restapi.user.entities.interfaces.user_email_interface import UserEmailInterface
from itsdangerous import URLSafeTimedSerializer
from django.core.mail import send_mail
import logging
from os import getenv, path, makedirs, getenv

class UserRepositoryAdapter(UserEmailInterface):

    def __init__(self, database) -> None:
        self.db = database()
    
    def generate_token(self, email):
        serializer = URLSafeTimedSerializer(getenv('SECRET_KEY'))
        return serializer.dumps(email, salt=getenv["SECURITY_PASSWORD_SALT"])
    
    def confirm_token(self, token, expiration):
        serializer = URLSafeTimedSerializer(getenv('SECRET_KEY'))
        try:
            email = serializer.loads(
                token, salt=getenv["SECURITY_PASSWORD_SALT"], max_age=expiration
            )
            return email
        except Exception:
            return False

    def send_email(email, token):
        send_mail(
            "Movies App confirmation token",
            "token: {token}".format(token=token),
            getenv("MAIL_DEFAULT_SENDER"),
            [email],
            fail_silently=False,
        )
        