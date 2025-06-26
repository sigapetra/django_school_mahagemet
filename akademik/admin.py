# akademik/admin.py

from django.contrib import admin
from .models import Kelas, Siswa, Guru # Import model-model yang baru dibuat

# Mendaftarkan model-model ke Admin Panel
admin.site.register(Kelas)
admin.site.register(Siswa)
admin.site.register(Guru)