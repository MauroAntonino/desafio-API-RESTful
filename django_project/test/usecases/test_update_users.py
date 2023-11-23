import unittest
from restapi.user.usecases.user_service import UserService
from test.helpers.user_repository_adapter_helper import UserRepositoryAdapterHelper
from test.helpers.user_email_adapter_helper import UserEmailAdapterHelper
from restapi.user.infra.repository.mysql import MySql
from os import path
import logging
from restapi.user.entities.objects.user import User
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')
logger = logging.getLogger(__name__)

userService = UserService(user_repository=UserRepositoryAdapterHelper(MySql), user_email=UserEmailAdapterHelper(MySql))

class TestUpdateUser(unittest.TestCase):

    def test_update_user_success(self):
        user = User(
            user_id=None,
            name="test test",
            password=None,
            email="test@email.com",
            image_url=None,
            is_confirmed=None
        )

        response = userService.update_user(user=user, image=None)
        self.assertEqual(response.get("user").get("name"), user.name)

    def test_create_user_invalid_email(self):
        user = User(
            user_id=None,
            name="test test",
            password="sdfsdfsdfsdfsdf",
            email="testemail.com",
            image_url=None,
            is_confirmed=None
        )

        with self.assertRaises(Exception):
            userService.update_user(user=user, image=None)

if __name__ == '__main__':
    unittest.main()