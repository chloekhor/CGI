from django.urls import path
from .views import register_view  # Import your view

urlpatterns = [
    path('api/register/', register_view, name='register'),  # Ensure correct path
]
