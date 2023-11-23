from restapi.user.entities.objects.user import User
from restapi.user.entities.interfaces.user_repository_interface import UserRepositoryInterface
from restapi.user.entities.interfaces.user_email_interface import UserEmailInterface

class UserService:

    def __init__(self, user_repository: UserRepositoryInterface, user_email: UserEmailInterface):
        self.user_repository :UserRepositoryInterface = user_repository
        self.user_email :UserEmailInterface = user_email
    
    def create_user(self, user: User, image):
        self.user_repository.validate_user(user)
        user = self.user_repository.create_user(user=user)
        self.user_repository.save_image(image=image, user=user)
        return {
            "user": user.__dict__
        }

    def auth_user(self, email, password):
        return self.user_repository.check_user(email=email, password=password)
    
    def get_movies(self, page_size, page, search, order):
        movies = self.user_repository.get_movies(page_size=page_size, page=page, search=search, order=order)
        return { "movies": [movie.__dict__ for movie in movies]}
    
    def get_best_movies(self, page_size, page, search, order, email):
        is_email = self.user_repository.is_email_checked(email)
        if (is_email):
            movies = self.user_repository.get_best_movies(page_size=page_size, page=page, search=search, order=order)
            return { "movies": [movie.__dict__ for movie in movies]}
        else:
            return {"msg": "user email is not checked"}

    def update_user(self, user: User, image):
        self.user_repository.validate_update_user(user)
        user = self.user_repository.update_user(user=user)
        self.user_repository.save_image(image=image, user=user)
        return {
            "user": user.__dict__
        }
    
    def send_token(self, email):
        token = self.user_email.generate_token(email)
        self.user_email.email_send_token(email=email, token=token)
    
    def confirm_email(self, user_email, token):
        email = self.user_email.confirm_token(token=token)
        if (user_email==email):
            self.user_repository.email_is_valid(email=email)
        else:
            raise Exception("Token is invalid")