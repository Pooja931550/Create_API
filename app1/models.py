from django.db import models
from django.contrib.auth.models import AbstractUser



# # Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    phone_no = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=150, unique=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


def __str__(self):
    return str(self.email)


# class Task(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     task_name = models.CharField(max_length=60, default='na')
#     task_date = models.DateField(null=True)
#     subject = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='task')




#     def __str__(self):
#         return self.name



