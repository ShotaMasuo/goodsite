from django.urls import path
from .views import index,newfunc, createfunc, createuser

urlpatterns = [
    path('index/', index, name="index"),
    path('new/', newfunc, name="newfunc"),
    path('create/', createfunc, name="createfunc"),
    path('createuser/', createuser, name="createuser"),
]