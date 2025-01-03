from django.db import models
from multiselectfield import MultiSelectField

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birthday = models.DateField()
    date_of_passing = models.DateField(null=True, blank=True)
    cause_of_death = models.CharField(max_length=50,
        choices = [
            ('severe_anemia', 'Severe Anemia'),
            ('thrombosis', 'Thrombosis (Blood clot)'),
            ('internal_bleeding', 'Internal Bleeding'),
            ('organ_failure', 'Organ Failure'),
            ('infection', 'Infection'),
            ('treatment_complications', 'Treatment Complications'),
        ],
        null=True,
        blank=True
    )
    other_cause_of_death = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    spayed_neutered = models.BooleanField(default=False)
    weight = models.FloatField()

    def __str__(self):
        return self.name
    
class Diagnosis(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    diagnostic_method = MultiSelectField(
        max_length=50,
        choices = [
            ('routine_bloodwork', 'Routine blood work'),
            ('vet_visit_symptoms', 'Symptoms presented during another vet visit'),
            ('emergency_visit', 'Emergency vet visit due to acute symptoms'),
            ('other', 'Other')
        ]
    )
    diagnostic_date = models.DateField()
    # RBC = models.IntegerField(null=True, blank=True)
    initial_symptoms = MultiSelectField(
        choices = [
            ('lethargy', 'Lethargy'),
            ('weakness', 'Weakness'),
            ('pale_gums', 'Pale gums'),
            ('fever', 'Fever'),
            ('loss_appetite', 'Loss of appetite'),
            ('vomiting', 'Vomiting'),
            ('diarrhea', 'Diarrhea'),
            ('jaundice', 'Jaundice'),
            ('difficulty_breathing', 'Difficulty breathing'),
            ('other', 'Other'),
        ]
    )
    other_initial_symptoms = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Diagnosis for {self.pet.name}"
    
class Treatment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    medications = models.JSONField()  # Storing medications as JSON
    duration = models.CharField(
        max_length=30,
        choices=[
            ('LT_1WEEK', '< 1 Week'),
            ('BETWEEN_1_2_WEEKS', '1-2 Weeks'),
            ('BETWEEN_3_5_WEEKS', '3-4 Weeks'),
            ('OVER_5_WEEKS', '5+ Weeks'),
        ]
    )
    RBC = models.IntegerField(null=True, blank=True)
    RET = models.IntegerField(null=True, blank=True)
    PCV = models.IntegerField(null=True, blank=True)
    treatment_adjusted = models.BooleanField(default=False)

    def __str__(self):
        return f"Treatment for {self.pet.name}"

class LongTermCare(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    quality_of_life = models.CharField(
        max_length=10,
        choices=[
            ('excellent', 'Excellent'),
            ('good', 'Good'),
            ('fair', 'Fair'),
            ('poor', 'Poor')
        ]
    )
    personality_changes = models.CharField(
        max_length=15,
        choices=[
            ('significant', 'Yes, significantly'),
            ('slight', 'Yes, slightly'),
            ('no', 'No')
        ]
    )
    recurrence = models.BooleanField(default=False)
    resources = models.TextField(blank=True, null=True)

class UploadedDocument(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    document = models.FileField(upload_to='vet_docs/', blank=True, null=True)

    def __str__(self):
        return f"Document for {self.pet.name}"

































# class Pet(models.Model):
#     name = models.CharField(max_length=100)
#     breed = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
#     spayed_neutered = models.BooleanField(default=False)
#     weight = models.FloatField()
#     known_conditions = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Diagnosis(models.Model):
#     pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
#     diagnostic_method = models.CharField(
#         max_length=50,
#         choices=[
#             ('routine_bloodwork', 'Routine blood work'),
#             ('vet_visit_symptoms', 'Symptoms presented during another vet visit'),
#             ('emergency_visit', 'Emergency vet visit due to acute symptoms'),
#             ('other', 'Other')
#         ]
#     )
#     other_diagnostic_method = models.CharField(max_length=200, blank=True, null=True)
#     initial_symptoms = MultiSelectField(
#         choices=[
#             ('lethargy', 'Lethargy'),
#             ('weakness', 'Weakness'),
#             ('pale_gums', 'Pale gums'),
#             ('fever', 'Fever'),
#             ('loss_appetite', 'Loss of appetite'),
#             ('vomiting', 'Vomiting'),
#             ('diarrhea', 'Diarrhea'),
#             ('jaundice', 'Jaundice'),
#             ('difficulty_breathing', 'Difficulty breathing'),
#             ('other', 'Other'),
#         ],
#         blank=True
#     )
#     other_initial_symptom = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"Diagnosis for {self.pet.name}"

# class TreatmentRound(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     medications = models.JSONField()  # Storing medications as JSON
#     duration = models.IntegerField(help_text="Duration in weeks")
#     side_effects = models.TextField(blank=True, null=True)
#     treatment_adjusted = models.BooleanField(default=False)
#     # Add RBC and measurement levels!!!

#     def __str__(self):
#         return f"Treatment for {self.pet.name}, Round {self.id}"

# class LongTermCare(models.Model):
#     pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
#     complications = models.TextField()
#     quality_of_life = models.CharField(
#         max_length=10,
#         choices=[
#             ('excellent', 'Excellent'),
#             ('good', 'Good'),
#             ('fair', 'Fair'),
#             ('poor', 'Poor')
#         ]
#     )
#     personality_changes = models.CharField(
#         max_length=15,
#         choices=[
#             ('significant', 'Yes, significantly'),
#             ('slight', 'Yes, slightly'),
#             ('no', 'No')
#         ]
#     )
#     recurrence = models.BooleanField(default=False)
#     resources = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Long-Term Care for {self.pet.name}"

# class UploadedDocument(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     document = models.FileField(upload_to='vet_docs/')

#     def __str__(self):
#         return f"Document for {self.pet.name}"



# _______
# SECOND DRAFT

# from django.contrib.auth.models import AbstractUserD
# from django.db import models
# from multiselectfield import MultiSelectField

# class Pet(models.Model):
#     name = models.CharField(max_length=100)
#     breed = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
#     spayed_neutered = models.BooleanField(default=False)
#     weight = models.FloatField()
#     known_conditions = models.TextField(blank=True, null=True)

# class Diagnosis(models.Model):
#     pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
#     diagnostic_method = models.CharField(
#         max_length=50,
#         choices=[
#             ('routine_bloodwork', 'Routine blood work'),
#             ('vet_visit_symptoms', 'Symptoms presented during another vet visit'),
#             ('emergency_visit', 'Emergency vet visit due to acute symptoms'),
#             ('other', 'Other')
#         ]
#     )
#     other_diagnostic_method = models.CharField(max_length=200, blank=True, null=True)
#     initial_symptoms = models.TextField()

# class TreatmentRound(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     round_number = models.IntegerField()
#     medications = models.JSONField()  # Store medication categories and details as JSON
#     duration = models.IntegerField(help_text="Duration in weeks")
#     side_effects = models.TextField(blank=True, null=True)
#     treatment_adjusted = models.BooleanField(default=False)

# class LongTermCare(models.Model):
#     pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
#     complications = models.TextField()
#     quality_of_life = models.CharField(
#         max_length=10,
#         choices=[
#             ('excellent', 'Excellent'),
#             ('good', 'Good'),
#             ('fair', 'Fair'),
#             ('poor', 'Poor')
#         ]
#     )
#     personality_changes = models.CharField(
#         max_length=15,
#         choices=[
#             ('significant', 'Yes, significantly'),
#             ('slight', 'Yes, slightly'),
#             ('no', 'No')
#         ]
#     )
#     recurrence = models.BooleanField(default=False)
#     resources = models.TextField(blank=True, null=True)

# class UploadedDocument(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     document = models.FileField(upload_to='vet_docs/')


# ________


# ___________
# FIRST DRAFT



# class Pet(models.Model):
#     pet_name = models.CharField(max_length=30, null=True, blank=True)
#     email = models.EmailField(max_length=254, null=True, blank=True)
#     birthday = models.DateTimeField()
#     diagnosis_date = models.DateTimeField()
#     # rbc_1 = models.IntegerField()
#     # pcv_1 = models.IntegerField()
#     # ret_1 = models.IntegerField()
#     blood_transfusion = models.BooleanField(default=False)
#     num_transfusions = models.IntegerField(null=True, blank=True)
#     # medication = models.BooleanField(default=False)

#     # Medications

#     # Immunosuppressants
#     prednisone = models.BooleanField(default=False)
#     dexamethasone = models.BooleanField(default=False)

#     # Secondary immunosuppressants
#     doxycycline = models.BooleanField(default=False)
#     cyclosporine = models.BooleanField(default=False)
#     mycophenolate = models.BooleanField(default=False)
#     azathioprine = models.BooleanField(default=False)

#     # Other
#     other_medications = models.CharField(max_length=200, null=True, blank=True)

#     additional_information = models.TextField(null=True, blank=True)
    
#     passing_date = models.DateTimeField(null=True, blank=True)
#     breed = models.CharField(max_length=30)
#     vaccinations = models.TextField()
#     # b_trans1 = models.BooleanField()
#     # # prescriptions = models.TextField()

#     PRESCRIPTION_CHOICES = [
#         ('antibiotic', 'Choice 1'),
#         ('painkiller', 'Painkiller'),
#         ('steroid', 'Steroid'),
#         ('immunosuppressant', 'Immunosuppressant'),
#     ]
#     # prescriptions = models.CharField(choices=PRESCRIPTION_CHOICES, null=True, blank=True)
#     # prescriptions = models.CharField(choices=PRESCRIPTION_CHOICES, null=True, blank=True, max_length=20)
#     prescriptions = MultiSelectField(choices=PRESCRIPTION_CHOICES, null=True, blank=True, max_length=20)
