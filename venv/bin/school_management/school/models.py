from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)  # Set a default class

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')  # Use 'students' as the related_name for clarity

    def __str__(self):
        return self.name
