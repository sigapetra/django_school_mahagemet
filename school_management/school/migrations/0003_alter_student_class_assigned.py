# Generated by Django 5.1.3 on 2024-11-06 02:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.class'),
        ),
    ]