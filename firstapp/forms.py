from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(required=False)
    lastName=forms.CharField()
    email=forms.CharField()
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField()


    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName)>20:
            raise forms.ValidationError('The max length of firstName is 20 Characters')
        return inputFirstName
    
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('Email should contain @')
        return inputEmail

