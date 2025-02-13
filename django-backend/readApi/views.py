from rest_framework import generics
from .models import History
from .serializers import HistorySerializer

class HistoryList(generics.ListAPIView):
    queryset = History.objects.all()  # Fetch all records from the history table
    serializer_class = HistorySerializer