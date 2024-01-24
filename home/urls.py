"""
This module handles the URL configurations for the 'home' app.
"""

from django.urls import path
from .views import Index


urlpatterns = [
    path('', Index.as_view(), name='home')
]