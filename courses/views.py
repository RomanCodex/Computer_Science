from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)

def course_details(request, id):
    course= Course.objects.get(id = id)
    context = {
        'course': course
    }
    return render(request, 'course.html', context)