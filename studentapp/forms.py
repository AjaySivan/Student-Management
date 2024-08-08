from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','number','age','enrollmentdate','course']

        labels = {
            'name' : 'Name',
            'email' : 'Email',
            'number' : 'Number',
            'age' : 'Age',
            'enrollmentdate' : 'Enrollment Date',
            'course' : 'Select Course',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.NumberInput(attrs={'class' : 'form-control','type':'number'}),
            'enrollmentdate' : forms.DateInput(attrs={'class' : 'form-control','type':'date'}),
            'course' : forms.Select(attrs={'class' : 'form-control'})
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')
        number = self.cleaned_data.get('number')
        if Student.objects.filter(name=name,number=number).exists():
            raise forms.ValidationError('Student already exists.')
        return name
        