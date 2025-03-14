# aiModel/urls.py

from django.urls import path
from . import views
from .views import upload_file  # 确保这里 import 了 upload_file 视图

urlpatterns = [
    path('api/upload/', views.upload_photo, name='upload_photo'),  # This maps the URL to the view
]
