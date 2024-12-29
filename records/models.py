from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


# class User(AbstractUser):
#     pass


class Pet(models.Model):
    pet_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    birthday = models.DateTimeField()
    diagnosis_date = models.DateTimeField()
    # rbc_1 = models.IntegerField()
    # pcv_1 = models.IntegerField()
    # ret_1 = models.IntegerField()
    blood_transfusion = models.BooleanField(default=False)
    num_transfusions = models.IntegerField(null=True, blank=True)
    # medication = models.BooleanField(default=False)

    # Medications

    # Immunosuppressants
    prednisone = models.BooleanField(default=False)
    dexamethasone = models.BooleanField(default=False)

    # Secondary immunosuppressants
    doxycycline = models.BooleanField(default=False)
    cyclosporine = models.BooleanField(default=False)
    mycophenolate = models.BooleanField(default=False)
    azathioprine = models.BooleanField(default=False)

    # Other
    other_medications = models.CharField(max_length=200, null=True, blank=True)

    additional_information = models.TextField(null=True, blank=True)
    
    passing_date = models.DateTimeField(null=True, blank=True)
    breed = models.CharField(max_length=30)
    vaccinations = models.TextField()
    # b_trans1 = models.BooleanField()
    # # prescriptions = models.TextField()

    PRESCRIPTION_CHOICES = [
        ('antibiotic', 'Choice 1'),
        ('painkiller', 'Painkiller'),
        ('steroid', 'Steroid'),
        ('immunosuppressant', 'Immunosuppressant'),
    ]
    # prescriptions = models.CharField(choices=PRESCRIPTION_CHOICES, null=True, blank=True)
    # prescriptions = models.CharField(choices=PRESCRIPTION_CHOICES, null=True, blank=True, max_length=20)
    prescriptions = MultiSelectField(choices=PRESCRIPTION_CHOICES, null=True, blank=True, max_length=20)
