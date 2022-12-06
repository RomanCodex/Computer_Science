from django.db import models
import os

# Create your models here.
class Lecturer(models.Model):
    name = models.CharField(max_length = 255)
    staff_id = models.CharField(max_length=16)
    certificates = models.CharField(max_length = 256)
    POST_CHOICES =(
        ("Graduate Assistant", "Graduate Assistant"),
        ("Assistant Lecturer", "Assistant Lecturer"),
        ("Lecturer Grade II", "Lecturer Grade II"),
        ("Lecturer Grade I", "Lecturer Grade I"),
        ("Senior Lecturer", "Senior Lecturer"),
        ("Associate Professor", "Associate Professor"),
        ("Professor", "Professor")
    )
    GENDER_CHOICES=(
        ("Male", "Male"), 
        ("Female", "Female")
    )
    post= models.CharField(max_length=255, choices=POST_CHOICES)
    gender= models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    bio = models.CharField(max_length = 140, blank=True)
    hobbies = models.CharField(max_length = 2048, blank=True)
    facebook_username = models.CharField(max_length= 255, blank=True)
    twitter_handle = models.CharField(max_length = 255, blank= True)
    github_username = models.CharField(max_length = 255, blank=True)

    def __str__(self):
        return self.name