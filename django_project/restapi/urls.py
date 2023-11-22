from django.urls import path, re_path

from restapi.user.adapters.controllers import create_user, login, get_movies, update_user, validate_email, get_best_movies, logout

urlpatterns = [
    path("user/", create_user.create_user, name="create_user"),
    path("user/update/", update_user.update_user, name="update_user"),
    path("login/", login.login, name="login"),
    path("logout/", logout.logout, name="logout"),
    path("images/<str:id>/", create_user.serve_image, name="serve_image"),
    path("movies/", get_movies.get_movies, name="get_movies"),
    path("movies/best/", get_best_movies.get_best_movies, name="get_best_movies"),
    path("email/", validate_email.validate_email, name="validate_email"),
    path("email/confirm/", validate_email.confirm_token, name="confirm_token"),
]