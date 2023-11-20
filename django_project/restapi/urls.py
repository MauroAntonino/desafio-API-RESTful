from django.urls import path, re_path

from restapi.controllers import views
from restapi.user.adapters.controllers import create_user, login, get_movies, update_user

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", create_user.create_user, name="create_user"),
    path("user/update/", update_user.update_user, name="update_user"),
    path("login/", login.login, name="login"),
    path("logout/", create_user.logout, name="logout"),
    path("images/<int:id>/<str:email>/", create_user.serve_image, name="serve_image"),
    path("movies", get_movies.get_movies, name="get_movies"),
]