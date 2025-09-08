from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, 5twin3.")

def bonjour(request):
    classe="5twin3"
    # Renders the template 'event/bonjour.html' from Event/templates/event/bonjour.html
    return render(request, 'event/hello.html', {'classeroom': classe})
