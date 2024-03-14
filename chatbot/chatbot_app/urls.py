# chatbot/urls.py

from django.urls import path
from .views import name_input_view

urlpatterns = [
    path('', name_input_view, name='name_input'),
]
