from django import forms
from .models import student2

class student_form(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(),  required=True, max_length=100)
    email_id = forms.EmailField(forms=forms.EmailField(), requird= True, max_length = 100)
    contact_no = forms.CharField(forms= forms.NumberInput(), requird= True, max_length=11)
    date = forms.DateTimeField(forms= forms.DateTimeField(),requird= True)


    class Meta():
        model = student2
        fields = ['name', 'email_id', 'contact_no', 'date']
        
