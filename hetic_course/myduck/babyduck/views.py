from django.shortcuts import render
from babyduck.models import Duck

def index (request) :
    listDuck = Duck.objects.all()
    return render(request , "index.html" , {
        'names' : listDuck[0].name
    })

def chat (request) :
    return render(request , "chat.html")

def happy (request) :
    return render(request , "chat_happy.html")

def sad(request) :
    return render(request , "chat_sad.html")

def angry(request) :
    return render(request , "chat_angry.html")