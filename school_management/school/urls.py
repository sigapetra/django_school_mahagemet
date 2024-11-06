from django.urls import path
from .views import (
    login_view, logout_view, index, student_list, class_list, teacher_list,
    create_student, update_student, delete_student,
    create_class, update_class, delete_class,
    create_teacher, update_teacher, delete_teacher,
    students_by_class, teachers_by_class
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', index, name='index'),
    path('students/', student_list, name='student_list'),
    path('students/create/', create_student, name='create_student'),
    path('students/update/<int:id>/', update_student, name='update_student'),
    path('students/delete/<int:id>/', delete_student, name='delete_student'),
    path('classes/', class_list, name='class_list'),
    path('classes/create/', create_class, name='create_class'),
    path('classes/update/<int:id>/', update_class, name='update_class'),
    path('classes/delete/<int:id>/', delete_class, name='delete_class'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', create_teacher, name='create_teacher'), 
    path('teachers/update/<int:id>/', update_teacher, name='update_teacher'),
    path('teachers/delete/<int:id>/', delete_teacher, name='delete_teacher'),
    path('classes/<int:class_id>/students/', students_by_class, name='students_by_class'),
    path('classes/<int:class_id>/teachers/', teachers_by_class, name='teachers_by_class'),
]
