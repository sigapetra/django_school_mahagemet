# akademik/serializers.py
from rest_framework import serializers
from .models import Kelas, Siswa, Guru

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = ['id', 'nama_kelas', 'deskripsi', 'tahun_ajaran']

class SiswaSerializer(serializers.ModelSerializer):
    kelas_nama = serializers.CharField(source='kelas.nama_kelas', read_only=True) # Untuk menampilkan nama kelas

    class Meta:
        model = Siswa
        fields = ['id', 'NIS', 'nama_lengkap', 'kelas', 'kelas_nama', 'tanggal_lahir', 'alamat']

class GuruSerializer(serializers.ModelSerializer):
    # Untuk menampilkan nama-nama kelas yang diajar guru
    kelas_diajar_nama = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Guru
        fields = ['id', 'NIP', 'nama_lengkap', 'mata_pelajaran', 'kelas_diajar', 'kelas_diajar_nama', 'tanggal_lahir', 'alamat']