# akademik/api_views.py

from rest_framework import viewsets
from .models import Kelas, Siswa, Guru
from .serializers import KelasSerializer, SiswaSerializer, GuruSerializer

# ViewSet untuk model Kelas
class KelasViewSet(viewsets.ModelViewSet):
    # queryset: Menentukan data yang akan diambil oleh ViewSet ini.
    # Kelas.objects.all() akan mengambil semua objek Kelas.
    queryset = Kelas.objects.all()
    # serializer_class: Menentukan serializer yang akan digunakan untuk mengonversi
    # objek model menjadi data yang bisa di-API-kan (misalnya JSON) dan sebaliknya.
    serializer_class = KelasSerializer

# ViewSet untuk model Siswa
class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

# ViewSet untuk model Guru
class GuruViewSet(viewsets.ModelViewSet):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer