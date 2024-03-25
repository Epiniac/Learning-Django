from django.shortcuts import render

def index (request) :
    return render(request , "index.html" )

def chat (request) :
    return render(request , "chat.html")

def happy (request) :
    return render(request , "chat_happy.html")

def sad(request) :
    return render(request , "chat_sad.html")

def angry(request) :
    return render(request , "chat_angry.html")