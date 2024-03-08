# chatbot/urls.py

from django.urls import path
from .views import chatbot_view, pdf_view

urlpatterns = [
    path('', chatbot_view, name='chatbot-app'),
    path('pdf_response/', pdf_view)
]
