from django.urls import path
from .views import HistoryList, ProfileList


urlpatterns = [
    path('api/history/', HistoryList.as_view(), name='history-list'),
    path('api/profile/', ProfileList.as_view(), name='profile-list'),
]