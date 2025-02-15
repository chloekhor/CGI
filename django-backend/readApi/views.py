from rest_framework import generics
from .models import History, Profile
from .serializers import HistorySerializer, ProfileSerializer

class HistoryList(generics.ListAPIView):
    queryset = History.objects.all()  # Fetch all records from the history table
    serializer_class = HistorySerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()  # Fetch all records from the profile table
    serializer_class = ProfileSerializer
