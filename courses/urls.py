from django.urls import path
from .views import all_courses, course_details

urlpatterns = [
    path("", all_courses, name='courses'),
    path("<int:id>/details/", course_details),
]