import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from users.models import Users  

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
