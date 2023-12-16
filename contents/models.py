from typing import Any
from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.name
class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    # Choices for the current role radio buttons
    ROLE_CHOICES = [
        ('student', 'student'),
        ('job', 'job'),
        ('learner', 'learner')
        # Add more choices as needed
    ]
    current_role = models.CharField(max_length=80, choices=ROLE_CHOICES, default='default_role_value')
    # Checkbox options for useful field
    RECOMMEND_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    recommend = models.CharField(max_length=50, choices=RECOMMEND_CHOICES,default='default_role_value')

    # Checkbox options for useful field
    USEFUL_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    useful = models.CharField(max_length=50, choices=USEFUL_CHOICES,default='default_role_value')

    message = models.TextField()
    username=models.CharField(max_length=100,default='superuser')

 



class form_d(models.Model):
    name=models.CharField( max_length=500)
    email=models.CharField( max_length=500)
    address=models.CharField( max_length=500)
    phone=models.CharField( max_length=500)
   
