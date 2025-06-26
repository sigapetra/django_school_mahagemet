# akademik/models.py
from django.db import models

# Model untuk Kelas
class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=100, unique=True, help_text="Contoh: X IPA 1, XI IPS 2")
    deskripsi = models.TextField(blank=True, null=True)
    tahun_ajaran = models.CharField(max_length=9, default="2024/2025", help_text="Format: YYYY/YYYY (misal: 2024/2025)")

    class Meta:
        verbose_name_plural = "Daftar Kelas" # Nama di admin panel
        ordering = ['nama_kelas'] # Mengurutkan berdasarkan nama kelas

    def __str__(self):
        return self.nama_kelas

# Model untuk Siswa
class Siswa(models.Model):
    NIS = models.CharField(max_length=20, unique=True, help_text="Nomor Induk Siswa")
    nama_lengkap = models.CharField(max_length=200)
    # Relasi ForeignKey: Setiap siswa terdaftar pada satu kelas
    kelas = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True, blank=True, related_name='siswa_di_kelas')
    tanggal_lahir = models.DateField(null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Daftar Siswa" # Nama di admin panel
        ordering = ['nama_lengkap'] # Mengurutkan berdasarkan nama siswa

    def __str__(self):
        return f"{self.nama_lengkap} ({self.NIS})"

# Model untuk Guru
class Guru(models.Model):
    NIP = models.CharField(max_length=20, unique=True, help_text="Nomor Induk Pegawai")
    nama_lengkap = models.CharField(max_length=200)
    mata_pelajaran = models.CharField(max_length=100, help_text="Contoh: Matematika, Bahasa Inggris")
    # Relasi ManyToManyField: Satu guru bisa mengajar banyak kelas, satu kelas bisa diajar banyak guru
    kelas_diajar = models.ManyToManyField(Kelas, related_name='guru_pengajar', blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Daftar Guru" # Nama di admin panel
        ordering = ['nama_lengkap'] # Mengurutkan berdasarkan nama guru

    def __str__(self):
        return f"{self.nama_lengkap} ({self.mata_pelajaran})"
