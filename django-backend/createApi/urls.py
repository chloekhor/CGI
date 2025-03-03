from django.urls import path
from .views import register_view, save_analysis   # Import your view

urlpatterns = [
    path('api/register/', register_view, name='register'),  # Ensure correct path
    path('api/save/', save_analysis , name='login'),  # Ensure correct path
]
