from django.urls import path
from .views import all_lecturers, lecturer_details

urlpatterns = [
    path("", all_lecturers, name='lecturers'),
    path("<int:id>/details/", lecturer_details)
]