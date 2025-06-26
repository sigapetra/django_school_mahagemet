# akademik/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required # Impor untuk membatasi akses
from .models import Kelas, Siswa, Guru

# --- Halaman Home/Dashboard Setelah Login ---
@login_required
def home(request):
    """
    Menyajikan halaman dashboard/home setelah login.
    """
    return render(request, 'akademik/home.html')

# --- Views untuk tampilan HTML biasa ---
def daftar_kelas(request):
    all_kelas = Kelas.objects.all()
    context = {'daftar_kelas': all_kelas}
    return render(request, 'akademik/daftar_kelas.html', context)

def detail_kelas(request, kelas_id):
    kelas = get_object_or_404(Kelas, pk=kelas_id)
    siswa_di_kelas = kelas.siswa_di_kelas.all()
    guru_pengajar = kelas.guru_pengajar.all()
    context = {
        'kelas': kelas,
        'siswa_di_kelas': siswa_di_kelas,
        'guru_pengajar': guru_pengajar,
    }
    return render(request, 'akademik/detail_kelas.html', context)

def daftar_semua(request):
    all_siswa = Siswa.objects.all()
    all_kelas = Kelas.objects.all()
    all_guru = Guru.objects.all()
    context = {
        'all_siswa': all_siswa,
        'all_kelas': all_kelas,
        'all_guru': all_guru,
    }
    return render(request, 'akademik/daftar_semua.html', context)

# --- Views untuk CRUD dengan Dummyjson.com ---
def crud_siswa_dummy(request):
    """Menyajikan halaman HTML untuk mengelola Siswa menggunakan dummyjson.com/users API."""
    return render(request, 'akademik/crud_siswa_dummy.html')

def crud_guru_dummy(request):
    """Menyajikan halaman HTML untuk mengelola Guru menggunakan dummyjson.com/users API."""
    return render(request, 'akademik/crud_guru_dummy.html')

def crud_kelas_dummy(request):
    """Menyajikan halaman HTML untuk mengelola Kelas menggunakan dummyjson.com/posts API."""
    return render(request, 'akademik/crud_kelas_dummy.html')

# --- Views untuk CRUD dengan Django API Lokal (tetap ada, meskipun frontend saat ini tidak menggunakannya) ---
@login_required
def kelola_siswa_api(request):
    """
    Menyajikan halaman untuk mengelola Siswa menggunakan Django REST Framework API.
    """
    return render(request, 'akademik/kelola_siswa_api.html')

@login_required
def kelola_guru_api(request):
    """
    Menyajikan halaman untuk mengelola Guru menggunakan Django REST Framework API.
    """
    return render(request, 'akademik/kelola_guru_api.html')

@login_required
def kelola_kelas_api(request):
    """
    Menyajikan halaman untuk mengelola Kelas menggunakan Django REST Framework API.
    """
    return render(request, 'akademik/kelola_kelas_api.html')

@login_required
def kelola_pengguna_dummy(request):
    """
    Menyajikan halaman untuk mengelola pengguna dummy menggunakan dummyjson.com/users API.
    """
    return render(request, 'akademik/kelola_pengguna_dummy.html')
