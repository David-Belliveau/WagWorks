from django import forms
from .models import Pet



# class PetDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Pet
        

class PetDetailsForm(forms.ModelForm):


    class Meta:
        
        model = Pet
        fields = [
            'pet_name',
            'breed',
            'email',
            'birthday',
            'passing_date',
            'diagnosis_date',
            'blood_transfusion',
            'num_transfusions',
            'prednisone',
            'dexamethasone',
            'doxycycline',
            'cyclosporine',
            'mycophenolate',
            'azathioprine',
            'other_medications',
            'additional_information',

            # 'vaccinations',
            # 'rbc_1',
            # 'pcv_1',
            # 'ret_1',
            'prescriptions'
        ]
        widgets = {
            'pet_name': forms.TextInput(attrs={'placeholder': 'e.g. Calvin', 'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'placeholder': 'e.g. Cocker Spaniel', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e.g. mario@example.com', 'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'diagnosis_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'blood_transfusion': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'num_transfusions': forms.NumberInput(attrs={'class': 'form-control', 'min':'0'}),

            'passing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vaccinations': forms.Textarea(attrs={'placeholder': 'Enter vaccinations as a comma-separated list', 'class': 'form-control'}),
            
            # Medications
            'prednisone' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            'dexamethasone' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            'doxycycline' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            'cyclosporine' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            'mycophenolate' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            'azathioprine' : forms.CheckboxInput(attrs={'class': 'form-check'}),
            # 'azathioprine' : forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
            'other_medications' : forms.TextInput(attrs={'placeholder': 'Please enter any related medications taken during treatment', 'class': 'form-control'}),
    
            'additional_information': forms.Textarea(attrs={
                'placeholder': 'Please include any relevant information we may have missed to help us better understand IMHA.', 
                'class': 'form-control',
                'rows' : 3
                }),
        }

    def clean_num_transfusions(self):
        num_transfusions = self.cleaned_data.get('num_transfusions')
        if num_transfusions and num_transfusions < 0:
            raise forms.ValidationError("Number of transfusions cannot be negative.")
        return num_transfusions



# Alternate formatting? https://www.youtube.com/watch?v=j-L_T66WGkY&t=355s

# class PetDetailsForm2(forms.ModelForm):

#     # PetNameField
#     pet_name = forms.TextInput(
#         label="Pet's name",
#         widget=forms.TextInput(
#             attrs={'placeholder': 'e.g. Calvin',
#                    'class': 'form-control'}
#         )
#     )

