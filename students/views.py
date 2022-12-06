from django.shortcuts import render
from .models import Student

# Create your views here.
def all_students(request):
    students = Student.objects.all()
    context ={
        'students': students
    }
    return render(request, 'students.html', context)

def student_details(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student': student
    }
    return render(request, 'student.html', context)