from restapi.user.entities.objects.user import User
from restapi.user.entities.interfaces.user_repository_interface import UserRepositoryInterface

class UserService:

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository :UserRepositoryInterface = user_repository
    
    def create_user(self, user: User, image):
        self.user_repository.validate_user(user)
        user = self.user_repository.create_user(user=user)
        self.user_repository.save_image(image=image)
        return {
            "user": user.__dict__
        }

    def auth_user(self, email, password):
        return self.user_repository.check_user(email=email, password=password)