from django import forms
from .models import Patient_Report

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient_Report
        fields = ['patient_name', 'mobile_no', 'weight', 'years_diabetes', 'leftRetina', 'rightRetina']
        
        