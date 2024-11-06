# project_name/urls.py (the main `urls.py` in your project folder)
from django.contrib import admin
from django.urls import path, include  # Ensure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the URLs from the api app
    path('fetch-students/', views.fetch_students_from_api, name='fetch_students'),  # Define the fetch-students route
]
