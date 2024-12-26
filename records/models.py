from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Pet(models.Model):
    email = models.EmailField(max_length=254, null=True, blank=True)
    birthday = models.DateTimeField()
    passing_date = models.DateTimeField()
    breed = models.TextField(default="Default content")
    diagnosis_date = models.DateTimeField()
    vaccinations = models.TextField()
    rbc_1 = models.IntegerField()
    pcv_1 = models.IntegerField()
    ret_1 = models.IntegerField()
    b_trans1 = models.BooleanField()
    prescriptions = models.TextField()
