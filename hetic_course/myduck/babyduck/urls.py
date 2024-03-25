from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index , name="index"),
    path('chat', views.chat ,name="chat"),
    path('angry', views.chat, name="angry"),
    path('happy', views.chat, name="happy"),
    path('sad', views.chat, name="sad"),
]