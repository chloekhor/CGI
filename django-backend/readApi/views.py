from rest_framework import generics
from .models import History
from .serializers import HistorySerializer, UsersSerializer

from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import Users  


class HistoryList(generics.ListAPIView):
    queryset = History.objects.all()  # Fetch all records from the history table
    serializer_class = HistorySerializer

class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()  # Fetch all records from the profile table
    serializer_class = UsersSerializer

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON
            email = data.get('email')
            password = data.get('password')

            print("Received login request: email={email}, password={password}")  # Debugging

            hashed_password = make_password(password)


            # Check if user exists
            user = Users.objects.filter(email=email).first()
            if not user:
                print("User not found")  # Debugging
                return JsonResponse({"error": "Invalid email"}, status=401)
            
            print("the userbthing", user.password)

            # Check password
            if check_password(hashed_password, user.password):
                print("Password incorrect")  # Debugging
                return JsonResponse({"error": "Invalid password"}, status=401)

            print("Login successful!")  # Debugging
            return JsonResponse({"message": "Login successful", "user_id": user.id, "email": user.email})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

