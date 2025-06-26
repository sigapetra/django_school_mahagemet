# school_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Impor built-in auth views
from akademik import views as akademik_views        # <--- Tambahkan baris ini


# Impor views dari aplikasi akademik
urlpatterns = [
    path('admin/', admin.site.urls),

    # URL untuk login dan logout (menggunakan built-in views Django)
    path('login/', auth_views.LoginView.as_view(template_name='akademik/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Mengarahkan root URL langsung ke home view dari aplikasi akademik
    path('', akademik_views.home, name='home'), # Ini akan menangani http://127.0.0.1:8000/

    # URL untuk aplikasi akademik
    path('akademik/', include('akademik.urls')),

    # URL untuk API Django REST Framework
    path('api-auth/', include('rest_framework.urls')),  # Ini akan menambahkan URL
    # untuk login/logout API jika Anda menggunakan DRF's browsable API. 


]