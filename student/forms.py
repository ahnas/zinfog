from dataclasses import field
from django import forms
from .models import Student
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,DateInput


class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'dob': DateInput (attrs={'type':'date','class': 'required form-control', 'placeholder': 'Date'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Location'}),
            'email': EmailInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email Address'}),
            'image': FileInput(attrs={'class': 'required form-control', 'placeholder': ''}),
        }