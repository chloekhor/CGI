# aiModel/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Prototype_v1 import evaluate_food_image  # Import your AI evaluation function
from .gemini_helper import get_gemini_recommendation # AI generate recommendation
from .CGI_all_in_one_v2 import main
from django.conf import settings
from urllib.parse import urljoin

import json
import os

BASE_URL = "http://localhost:8000"

@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        if 'photo' in request.FILES:
            photo = request.FILES['photo']

            target_values = request.POST.get('target')
            target_values = json.loads(target_values)
                
            # Save the file temporarily
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, photo.name)
            with open(file_path, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)

            photo_url = urljoin(BASE_URL, f"{settings.MEDIA_URL}uploads/{photo.name}")
            # Call your AI model evaluation function here
            evaluation_result = main(file_path)

            recommendation = get_gemini_recommendation(evaluation_result, target_values)

            # Return the evaluation result
            return JsonResponse({'message': 'File uploaded successfully', 'evaluation': evaluation_result,'target': target_values,'recommendation': recommendation, 'photo_url': photo_url})
        else:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
