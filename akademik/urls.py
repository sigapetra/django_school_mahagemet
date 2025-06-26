# akademik/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import KelasViewSet, SiswaViewSet, GuruViewSet

# Buat Router baru (Untuk API Django Lokal)
router = DefaultRouter()
router.register(r'kelas-api', KelasViewSet)
router.register(r'siswa-api', SiswaViewSet)
router.register(r'guru-api', GuruViewSet)

urlpatterns = [
    # --- URL untuk tampilan HTML biasa ---
    path('kelas/', views.daftar_kelas, name='daftar_kelas'),
    path('kelas/<int:kelas_id>/', views.detail_kelas, name='detail_kelas'),
    path('semua/', views.daftar_semua, name='daftar_semua'),

    # --- URL untuk CRUD dengan Dummyjson.com ---
    path('crud-siswa-dummy/', views.crud_siswa_dummy, name='crud_siswa_dummy'),
    path('crud-guru-dummy/', views.crud_guru_dummy, name='crud_guru_dummy'),
    path('crud-kelas-dummy/', views.crud_kelas_dummy, name='crud_kelas_dummy'),

    # --- URL untuk CRUD dengan Django API Lokal ---
    path('kelola-siswa-api/', views.kelola_siswa_api, name='kelola_siswa_api'),
    path('kelola-guru-api/', views.kelola_guru_api, name='kelola_guru_api'),
    path('kelola-kelas-api/', views.kelola_kelas_api, name='kelola_kelas_api'),

    # --- URL untuk API Django Lokal ---
    path('api/', include(router.urls)),
]
