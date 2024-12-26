from django import forms
from .models import Pet



class PetDetailsForm(forms.ModelForm):
    class Meta:
        model = Pet
        

class PetDetailsForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'email',
            'birthday',
            'passing_date',
            'breed',
            'diagnosis_date',
            'vaccinations',
            'rbc_1',
            'pcv_1',
            'ret_1',
            'b_trans1',
            'prescriptions'
        ]
        widgets = {
            'email': forms.TextArea(attrs={'placeholder': 'Optional'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'passing_date': forms.DateInput(attrs={'type': 'date'}),
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'vaccinations': forms.Textarea(attrs={'placeholder': 'Enter vaccinations as a comma-separated list'}),
            'prescriptions': forms.Textarea(attrs={'placeholder': 'Enter prescriptions as a comma-separated list'}),
        }