from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from auth_app import views

urlpatterns = [
    path('/login', csrf_exempt(views.login), name='create_paragraph')
]