from rest_framework import serializers
from .models import History
from users.models import Users


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'  # Include all fields in the API response

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'