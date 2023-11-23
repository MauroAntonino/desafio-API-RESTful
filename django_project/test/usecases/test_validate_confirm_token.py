import unittest
from restapi.user.usecases.user_service import UserService
from test.helpers.user_repository_adapter_helper import UserRepositoryAdapterHelper
from test.helpers.user_email_adapter_helper import UserEmailAdapterHelper
from restapi.user.infra.repository.mysql import MySql
from os import path

userService = UserService(user_repository=UserRepositoryAdapterHelper(MySql), user_email=UserEmailAdapterHelper(MySql))

class TestValidateConfirmToken(unittest.TestCase):

    def test_confirm_valid_token(self):
        email = "test@email.com"
        token = UserEmailAdapterHelper().generate_token(email=email)

        userService.confirm_email(email, token)

    def test_create_user_invalid_email(self):
        email = "test@email.com"
        invalid_email = "test_invalid@email.com"
        token = UserEmailAdapterHelper().generate_token(email=email)

        with self.assertRaises(Exception):
            userService.confirm_email(invalid_email, token)

if __name__ == '__main__':
    unittest.main()