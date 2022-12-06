from django.urls import path
from .views import all_students, student_details

urlpatterns = [
    path("", all_students, name='students'),
    path("<int:id>/details", student_details, name='students_details')
]