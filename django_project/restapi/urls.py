from django.urls import path

from restapi.controllers import views

urlpatterns = [
    path("", views.index, name="index"),
]