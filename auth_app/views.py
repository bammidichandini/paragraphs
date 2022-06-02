import json
import uuid

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token

def login(request):
    body = json.loads(request.body)
    username = body.get("username")
    password = body.get("password")

    user = User.objects.get(username=username)
    if user.check_password(password):
        token = Token.objects.get_or_create(user=user)

        return HttpResponse(json.dumps(token[0].key))

    return HttpResponseForbidden(headers={"X-Frame-Options": "Content-Security-Policy"})
