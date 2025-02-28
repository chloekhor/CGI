from django.urls import path
from .views import HistoryList, UsersList, login_view


urlpatterns = [
    path('api/history/', HistoryList.as_view(), name='history-list'),
    path('api/profile/', UsersList.as_view(), name='profile-list'),
    path('api/login/', login_view, name='login'),
    
]