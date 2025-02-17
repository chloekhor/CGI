# aiModel/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Prototype_v1 import evaluate_food_image  # Import your AI evaluation function

import os

@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
            
            # Save the file temporarily
            upload_dir = 'uploads/'
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, photo.name)
            with open(file_path, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)
            
            # Call your AI model evaluation function here
            evaluation_result = evaluate_food_image(file_path)

            # Return the evaluation result
            return JsonResponse({'message': 'File uploaded successfully', 'evaluation': evaluation_result})
        else:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
