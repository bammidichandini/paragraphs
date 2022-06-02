from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core_app.views import create_paragraph, \
    get_paragraph

urlpatterns = [
    path('/paragraph/add', create_paragraph.CreateParagraph.as_view(), name='create_paragraph'),
    path('/paragraph/get', get_paragraph.GetParagraph.as_view(), name='get_paragraph'),
]