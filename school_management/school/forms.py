from django import forms
from .models import Student, Teacher, Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'class_assigned']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']  # Ensure this matches the field name in your model


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']
