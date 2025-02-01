import os
from django.db import models
from django.contrib.auth.models import User

def student_name_dict(instance, filename):
    return f'students/{instance.name}/{filename}'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    image = models.ImageField(upload_to=student_name_dict,default='default/images_1.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
