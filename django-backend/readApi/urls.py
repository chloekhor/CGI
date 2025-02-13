from django.urls import path
from .views import HistoryList

urlpatterns = [
    path('api/history/', HistoryList.as_view(), name='history-list'),
]