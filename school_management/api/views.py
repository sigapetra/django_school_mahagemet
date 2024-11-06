# api/views.py
from django.http import JsonResponse
import requests
from .models import Student

def fetch_students_from_api(request):
    url = 'https://dummyjson.com/students'  # Example endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Assuming data['students'] contains a list of students
        for item in data['students']:
            student = Student(
                name=item['name'],
                class_assigned=None  # Adjust this based on your model
            )
            student.save()

        return JsonResponse({'status': 'success', 'message': 'Students added successfully!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to fetch data from the API'})
