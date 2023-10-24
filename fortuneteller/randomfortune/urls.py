# Imports
from django.urls import path 
from . import views

# Fortune view
urlpatterns = [
  path("", views.fortune)
]