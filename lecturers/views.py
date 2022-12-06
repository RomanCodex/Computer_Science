from django.shortcuts import render
from .models import Lecturer

# Create your views here.
def all_lecturers(request):
    lecturers = Lecturer.objects.all()
    context = {
        'lecturers': lecturers
    }
    return render(request, 'lecturers.html', context)

def lecturer_details(request, id):
    lecturer = Lecturer.objects.get(id = id)
    context = {
        'lecturer': lecturer
    }
    return render(request, 'lecturer.html', context)