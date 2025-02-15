from rest_framework import serializers
from .models import History, Profile

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'  # Include all fields in the API response

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'profile_picture']