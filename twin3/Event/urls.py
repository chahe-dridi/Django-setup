from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('bonjour/', views.bonjour, name='bonjour'),  # Add this line
]
