from django.urls import path
# from .views import register

from view2 import login, register



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),  # 新增的登录 API
]
