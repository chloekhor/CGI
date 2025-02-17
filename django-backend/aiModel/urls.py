# aiModel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.upload_photo, name='upload_photo'),  # This maps the URL to the view
]
