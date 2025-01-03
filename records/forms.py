from django import forms
from .models import Pet, Diagnosis, Treatment, LongTermCare, UploadedDocument

class PetInfoForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'birthday', 'date_of_passing', 'cause_of_death','other_cause_of_death', 'gender', 'spayed_neutered', 'weight']

# class DiagnosisForm(forms.ModelForm):
#     # Custom behavior for initial symptoms
#     initial_symptoms = forms.MultipleChoiceField(
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
#         widget=forms.CheckboxSelectMultiple,
#         label="What were the initial symptoms your dog exhibited?",
#     )
#     other_initial_symptom = forms.CharField(
#         max_length=255, required=False, label="If Other, please specify"
#     )

#     class Meta:
#         model = Diagnosis
#         fields = ['diagnostic_method', 'other_diagnostic_method']

# class TreatmentForm(forms.Form):
#     # JSONField is used in the model, but we simplify input here
#     medications = forms.MultipleChoiceField(
#         choices=[
#             ('cyclosporine', 'Cyclosporine'),
#             ('azathioprine', 'Azathioprine'),
#             ('mycophenolate', 'Mycophenolate Mofetil'),
#             ('prednisone', 'Prednisone'),
#             ('prednisolone', 'Prednisolone'),
#             ('omeprazole', 'Omeprazole'),
#             ('famotidine', 'Famotidine'),
#             ('other', 'Other'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         label="Medications used",
#     )
#     duration = forms.IntegerField(label="Duration of treatment (in weeks)")
#     side_effects = forms.CharField(widget=forms.Textarea, label="Side Effects Observed", required=False)
#     treatment_adjusted = forms.BooleanField(label="Did the treatment change?", required=False)

# class LongTermCareForm(forms.ModelForm):
#     class Meta:
#         model = LongTermCare
#         fields = ['complications', 'quality_of_life', 'personality_changes', 'recurrence', 'resources']

# class UploadedDocumentForm(forms.ModelForm):
#     class Meta:
#         model = UploadedDocument
#         fields = ['document']






# ___________
# SECOND DRAFT
# class PetInfoForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = ['name', 'breed', 'age', 'gender', 'spayed_neutered', 'weight', 'known_conditions']

# class DiagnosisForm(forms.ModelForm):
#     class Meta:
#         model = Diagnosis
#         fields = ['diagnostic_method', 'other_diagnostic_method', 'initial_symptoms']

# class TreatmentRoundForm(forms.Form):
#     medications = forms.MultipleChoiceField(
#         choices=[
#             ('cyclosporine', 'Cyclosporine'),
#             ('azathioprine', 'Azathioprine'),
#             ('mycophenolate', 'Mycophenolate Mofetil'),
#             ('prednisone', 'Prednisone'),
#             ('prednisolone', 'Prednisolone'),
#             ('omeprazole', 'Omeprazole'),
#             ('famotidine', 'Famotidine'),
#             ('other', 'Other'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#     )
#     duration = forms.IntegerField(label="Duration of treatment (in weeks)")
#     side_effects = forms.CharField(widget=forms.Textarea, label="Side Effects Observed", required=False)
#     treatment_adjusted = forms.BooleanField(label="Did the treatment change?", required=False)

# class LongTermCareForm(forms.ModelForm):
#     class Meta:
#         model = LongTermCare
#         fields = ['complications', 'quality_of_life', 'personality_changes', 'recurrence', 'resources']

# class UploadedDocumentForm(forms.ModelForm):
#     class Meta:
#         model = UploadedDocument
#         fields = ['document']

# ___________

# ____________________

# class PetInfoForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Pet's Name")
#     email = forms.EmailField(required=False)
#     breed = forms.CharField(max_length=100, label="Breed")
#     birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Birth Date")
#     diagnosis_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Diagnosis Date")
#     passing_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Passing Date", required=False)


# class TreatmentForm(forms.Form):
#     number_rounds = forms.IntegerField(widget=forms.HiddenInput())
#     treatment_changed = forms.BooleanField(label="Did treatment change after this round?", required=False)
#     prescriptions = forms.MultipleChoiceField(
#         choices=[
#             ('prednisone', 'Prednisone'),
#             ('cyclosporine', 'Cyclosporine'),
#             ('azathioprine', 'Azathioprine'),
#             ('other', 'Other'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     other_prescription = forms.CharField(
#         label="Other prescription (if selected)",
#         widget=forms.Textarea,
#         required=False
#     )
#     blood_transfusion = forms.IntegerField()

# # Formset for multiple rounds
# TreatmentRoundFormSet = formset_factory(TreatmentRoundForm, extra=1)

# class PrescriptionForm(forms.Form):
#     prescription_name = forms.CharField(max_length=100, label="Medication Name")
#     dosage = forms.CharField(max_length=50, label="Dosage")
#     duration = forms.IntegerField(label="Duration (in days)")

# class TreatmentForm(forms.Form):
#     treatment_type = forms.CharField(max_length=100, label="Type of Treatment")
#     treatment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date")
#     notes = forms.CharField(widget=forms.Textarea, label="Additional Notes", required=False)

# class ExtraInfoForm(forms.Form):
#     additional_info = forms.CharField(widget=forms.Textarea, label="Any additional information?", required=False)





# class PetDetailsForm(forms.ModelForm):


#     class Meta:
        
#         model = Pet
#         fields = [
#             'pet_name',
#             'breed',
#             'email',
#             'birthday',
#             'passing_date',
#             'diagnosis_date',
#             'blood_transfusion',
#             'num_transfusions',
#             'prednisone',
#             'dexamethasone',
#             'doxycycline',
#             'cyclosporine',
#             'mycophenolate',
#             'azathioprine',
#             'other_medications',
#             'additional_information',

#             # 'vaccinations',
#             # 'rbc_1',
#             # 'pcv_1',
#             # 'ret_1',
#             'prescriptions'
#         ]
#         widgets = {
#             'pet_name': forms.TextInput(attrs={'placeholder': 'e.g. Calvin', 'class': 'form-control'}),
#             'breed': forms.TextInput(attrs={'placeholder': 'e.g. Cocker Spaniel', 'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'e.g. mario@example.com', 'class': 'form-control'}),
#             'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'diagnosis_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'blood_transfusion': forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'num_transfusions': forms.NumberInput(attrs={'class': 'form-control', 'min':'0'}),

#             'passing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'vaccinations': forms.Textarea(attrs={'placeholder': 'Enter vaccinations as a comma-separated list', 'class': 'form-control'}),
            
#             # Medications
#             'prednisone' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'dexamethasone' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'doxycycline' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'cyclosporine' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'mycophenolate' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             'azathioprine' : forms.CheckboxInput(attrs={'class': 'form-check'}),
#             # 'azathioprine' : forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
#             'other_medications' : forms.TextInput(attrs={'placeholder': 'Please enter any related medications taken during treatment', 'class': 'form-control'}),
    
#             'additional_information': forms.Textarea(attrs={
#                 'placeholder': 'Please include any relevant information we may have missed to help us better understand IMHA.', 
#                 'class': 'form-control',
#                 'rows' : 3
#                 }),
#         }

#     def clean_num_transfusions(self):
#         num_transfusions = self.cleaned_data.get('num_transfusions')
#         if num_transfusions and num_transfusions < 0:
#             raise forms.ValidationError("Number of transfusions cannot be negative.")
#         return num_transfusions



# # Alternate formatting? https://www.youtube.com/watch?v=j-L_T66WGkY&t=355s

# # class PetDetailsForm2(forms.ModelForm):

# #     # PetNameField
# #     pet_name = forms.TextInput(
# #         label="Pet's name",
# #         widget=forms.TextInput(
# #             attrs={'placeholder': 'e.g. Calvin',
# #                    'class': 'form-control'}
# #         )
# #     )

