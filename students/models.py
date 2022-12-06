from django.db import models
import os

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 255)
    registration_number = models.CharField(max_length=16)
    GENDER_CHOICES=(
        ("Male", "Male"), 
        ("Female", "Female")
    )
    gender= models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    LEVEL_CHOICES=(
        ("Level 1", "Level 1"),
        ("Level 2", "Level 2"), 
        ("Level 3", "Level 3"), 
        ("Level 4", "Level 4")
    )
    level = models.CharField(max_length= 8, choices=LEVEL_CHOICES)
    bio = models.CharField(max_length = 140, blank=True)
    hobbies = models.CharField(max_length = 2048, blank=True)
    facebook_username = models.CharField(max_length= 255, blank=True)
    twitter_handle = models.CharField(max_length = 255, blank= True)
    github_username = models.CharField(max_length = 255, blank=True)

    def __str__(self):
        return self.name