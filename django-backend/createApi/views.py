import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from users.models import Users, History

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            photo_url = data.get('photo_url', '')  # Optional

            hashed_password = make_password(password)

            print(f"Registering user: email={email}, password={password}")

            # Check if email already exists
            if Users.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already registered"}, status=400)

            # Create and save user
            user = Users(name=name, email=email, password=hashed_password, photo_url=photo_url)
            user.save()

            return JsonResponse({
                "message": "User registered successfully",
                "user_id": user.id,
                "email": user.email
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def save_analysis(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received Data:", data)

            evaluation_result = data.get('evaluation')
            recommendation = data.get('recommendation')
            target = data.get('target')
            photo_url = data.get('photo_url')

            # Get user session ID
            user_id = request.session.get("user_id")
            if not user_id:
                return JsonResponse({"error": "User ID not found in session"}, status=400)

            # Check if user exists
            try:
                user = Users.objects.get(id=user_id)
            except Users.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

            # Save to History table
            history_entry = History.objects.create(
                user=user,
                target=target,
                result=evaluation_result,
                suggestion=recommendation,
                photo=photo_url
            )

            return JsonResponse({"message": "Data saved successfully", "history_id": history_entry.id}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
