from django.urls import path
from .views import HistoryList, UsersList, login_view, get_user_session, update_profile_view


urlpatterns = [
    path('api/history/', HistoryList.as_view(), name='history-list'),
    path('api/profile/', UsersList.as_view(), name='profile-list'),
    path('api/login/', login_view, name='login'),
    path('api/session/', get_user_session, name='session-check'),
    path('api/profile/update/', update_profile_view, name='profile-update'),
]