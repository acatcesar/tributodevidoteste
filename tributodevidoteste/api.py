
from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.security import HttpBearer
from ninja.security import HttpBasicAuth
from django.contrib import auth

from meuapp.api import router as usuario_router


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = auth.authenticate(username=username, password=password)
        if user:
            return user.id


api = NinjaAPI(auth=BasicAuth())

api.add_router('/usuario', usuario_router)