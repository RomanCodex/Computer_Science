from django.db import models
import os

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length= 255)
    course_code = models.CharField(max_length = 7)
    LEVEL_CHOICES=(
        ("Level 1", "Level 1"), 
        ("Level 2", "Level 2"), 
        ("Level 3", "Level 3"),
        ("Level 4", "Level 4")
    )
    level = models.CharField(max_length = 10, choices= LEVEL_CHOICES)
    SEMESTER_CHOICES= (
        ("First Semester", "First Semester"), 
        ("Second Semester", "Second Semester")
    )
    semester = models.CharField(max_length = 30, choices = SEMESTER_CHOICES)
    lecturers = models.CharField(max_length= 2048)
    reference_text = models.CharField(max_length = 2048)

    def __str__(self):
        return self.course_title
