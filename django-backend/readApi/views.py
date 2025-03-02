from rest_framework import generics
from .models import History
from .serializers import HistorySerializer, UsersSerializer

from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import Users  


class HistoryList(generics.ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        # print("Session Key in get_queryset:", self.request.session.session_key)
        # print("User ID in get_queryset:", self.request.session.get("user_id"))

        # print("get_queryset is being called!")  # Debugging
        user_id = self.request.session.get("user_id")
        # print("user_id:", user_id)  # Debugging

        if user_id:
            return History.objects.filter(user_id=user_id)  # Fetch history records for the user
        return History.objects.none()  # Return empty queryset if no user_id


class UsersList(generics.ListAPIView):
    print("fuckkkk")
    serializer_class = UsersSerializer

    def get_queryset(self):
        print("get_queryset is being called!")  # Debugging
        
        user_id = self.request.session.get("user_id")
        print("userifffff", user_id)  # Debugging

        if user_id:
            return Users.objects.filter(id=user_id)
        return Users.objects.none()


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            user = Users.objects.filter(email=email).first()
            if not user:
                return JsonResponse({"error": "Invalid email"}, status=401)

            if not check_password(password, user.password):
                return JsonResponse({"error": "Invalid password"}, status=401)

            
            request.session.create()
            request.session["user_id"] = user.id
            request.session.modified = True
            request.session.save()  # 🔹 Ensure it persists

            print("Stored Session Data:", request.session.items())  # Debugging
            print("Session Key after login:", request.session.session_key)  # Debugging
            print("User ID stored in session:", request.session.get("user_id"))  # Debugging

            return JsonResponse({
                "message": "Login successful",
                "user_id": user.id,
                "email": user.email
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_user_session(request):
    """Check if the user is logged in by retrieving session user_id"""
    if request.method == 'GET':
        user_id = request.session.get("user_id", None)
        if user_id:
            return JsonResponse({"user_id": user_id})
        return JsonResponse({"error": "No active session"}, status=401)

    return JsonResponse({"error": "Invalid request method"}, status=405)



@csrf_exempt
def update_profile_view(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)

        user_id = data.get('user_id')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        user = Users.objects.filter(id=user_id).first()

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        user.name = name
        user.email = email
        if password:
            user.password = make_password(password)

        user.save()

        return JsonResponse({"message": "Profile updated successfully!"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)