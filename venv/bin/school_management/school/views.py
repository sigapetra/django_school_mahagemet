from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import StudentForm, TeacherForm, ClassForm
from .models import Class, Teacher, Student
from django.views.decorators.csrf import csrf_exempt
import json

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'school/index.html')

def student_list(request):
    students = Student.objects.all()
    print(f"Students: {students}")  # Debugging line
    return render(request, 'school/student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan student baru ke database
            return redirect('student_list')  # Redirect ke halaman daftar student
    else:
        form = StudentForm()
    return render(request, 'school/create_student.html', {'form': form})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        # Check if the request is JSON or form data
        if request.content_type == "application/json":
            # Parse JSON data
            try:
                data = json.loads(request.body)
                student.name = data.get('name', student.name)
                class_id = data.get('class', student.class_assigned_id)
                student.class_assigned = Class.objects.get(id=class_id)
                student.save()
                return JsonResponse({'status': 'success', 'id': student.id})
            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
        else:
            # Parse form data
            name = request.POST.get('name')
            class_id = request.POST.get('class')
            if name and class_id:
                student.name = name
                student.class_assigned = Class.objects.get(id=class_id)
                student.save()
                return JsonResponse({'status': 'success', 'id': student.id})

    classes = Class.objects.all()
    return render(request, 'school/update_student.html', {'student': student, 'classes': classes})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return JsonResponse({'status': 'success'})
    return render(request, 'school/delete_student_confirm.html', {'student': student})


def class_list(request):
    classes = Class.objects.all()  # Fetch all Class instances
    return render(request, 'school/class_list.html', {'classes': classes})


def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan class baru ke database
            return redirect('class_list')  # Redirect ke halaman daftar class
    else:
        form = ClassForm()
    return render(request, 'school/create_class.html', {'form': form})

# Update an existing class
def update_class(request, id):
    class_instance = get_object_or_404(Class, id=id)

    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            form.save()
            return redirect('class_list')  # Redirect after successful update
    else:
        form = ClassForm(instance=class_instance)

    return render(request, 'school/update_class.html', {'class_instance': class_instance, 'form': form})

# Delete a class
def delete_class(request, id):
    class_instance = get_object_or_404(Class, id=id)
    if request.method == "POST":
        class_instance.delete()
        return JsonResponse({'status': 'success'})
    return render(request, 'school/delete_class_confirm.html', {'class': class_instance})

def teacher_list(request):
    teachers = Teacher.objects.all()  # Retrieve all teachers
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new teacher to the database
            return redirect('teacher_list')  # Redirect to the teacher list page
    else:
        form = TeacherForm()
    return render(request, 'school/create_teacher.html', {'form': form})
    
def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'id': teacher.id})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form is invalid'})  # Handle form errors
    else:
        form = TeacherForm(instance=teacher)  # Prefill form with the existing teacher data
    return render(request, 'school/update_teacher.html', {'form': form})


def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher.delete()  # Delete the teacher
        return JsonResponse({'status': 'success'})
    return render(request, 'school/delete_teacher_confirm.html', {'teacher': teacher})


def students_by_class(request, class_id):
    # Get the class by ID
    class_instance = Class.objects.get(id=class_id)
    
    # Fetch all students associated with this class
    students = Student.objects.filter(class_assigned=class_instance)
    
    return render(request, 'school/students_by_class.html', {
        'class': class_instance,
        'students': students
    })

def teachers_by_class(request, class_id):
    # Get the class by ID
    class_instance = Class.objects.get(id=class_id)
    
    # Fetch all teachers associated with this class
    teachers = Teacher.objects.filter(class_assigned=class_instance)
    
    return render(request, 'school/teachers_by_class.html', {
        'class': class_instance,
        'teachers': teachers
    })

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

