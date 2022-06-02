from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core_app.views import create_paragraph, \
    get_paragraph

urlpatterns = [
    path('/paragraph/add', csrf_exempt(create_paragraph.create_paragraph), name='create_paragraph'),
    path('/paragraph/get', csrf_exempt(get_paragraph.get_paragraph), name='get_paragraph'),
]