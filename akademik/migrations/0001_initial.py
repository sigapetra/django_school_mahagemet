# Generated by Django 5.2.3 on 2025-06-20 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kelas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nama_kelas",
                    models.CharField(
                        help_text="Contoh: X IPA 1, XI IPS 2",
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("deskripsi", models.TextField(blank=True, null=True)),
                (
                    "tahun_ajaran",
                    models.CharField(
                        default="2024/2025",
                        help_text="Format: YYYY/YYYY (misal: 2024/2025)",
                        max_length=9,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Daftar Kelas",
                "ordering": ["nama_kelas"],
            },
        ),
        migrations.CreateModel(
            name="Guru",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "NIP",
                    models.CharField(
                        help_text="Nomor Induk Pegawai", max_length=20, unique=True
                    ),
                ),
                ("nama_lengkap", models.CharField(max_length=200)),
                (
                    "mata_pelajaran",
                    models.CharField(
                        help_text="Contoh: Matematika, Bahasa Inggris", max_length=100
                    ),
                ),
                ("tanggal_lahir", models.DateField(blank=True, null=True)),
                ("alamat", models.TextField(blank=True, null=True)),
                (
                    "kelas_diajar",
                    models.ManyToManyField(
                        blank=True, related_name="guru_pengajar", to="akademik.kelas"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Daftar Guru",
                "ordering": ["nama_lengkap"],
            },
        ),
        migrations.CreateModel(
            name="Siswa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "NIS",
                    models.CharField(
                        help_text="Nomor Induk Siswa", max_length=20, unique=True
                    ),
                ),
                ("nama_lengkap", models.CharField(max_length=200)),
                ("tanggal_lahir", models.DateField(blank=True, null=True)),
                ("alamat", models.TextField(blank=True, null=True)),
                (
                    "kelas",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="siswa_di_kelas",
                        to="akademik.kelas",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Daftar Siswa",
                "ordering": ["nama_lengkap"],
            },
        ),
    ]
