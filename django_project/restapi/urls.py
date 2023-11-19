from django.urls import path

from restapi.controllers import views
from restapi.user.adapters.controllers import create_user, login

urlpatterns = [
    path("", views.index, name="index"),
    path("user", create_user.create_user, name="create_user"),
    path("login", login.login, name="login"),
    path("logout", create_user.logout, name="logout"),
]