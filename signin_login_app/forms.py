from django import forms
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator


class SignUp(forms.Form):
    name = forms.CharField(required=False,label='',max_length=100, validators=[MinLengthValidator(1,'Minimum')],
                           widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}))
    email = forms.EmailField(required=False,label='',max_length=100, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    username = forms.CharField(required=False,label='',max_length=100, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Name'}))
    qualification = forms.CharField(required=False,label='',max_length=100, min_length=1,
                                    widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Qualification'}))
    password = forms.CharField(required=False,label='',min_length=8,max_length=100,widget=forms.TextInput
               (attrs={'class': 'form-control','placeholder': 'Password', 'type':'password'}))
    date_of_birth = forms.DateField(required=False,label='',widget=forms.TextInput
               (attrs={'class': 'form-control','placeholder': 'Password', 'type':'date'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        print (email)
        validator = EmailValidator()
        try:
            validator(email)
            print(email)
        except:
            raise forms.ValidationError("Email is not valid")
        return email

    def clean_name(self):
        print('aaaaaaaaaaa')
        name = self.cleaned_data['name']
        validator = MinLengthValidator(1)
        try:
            validator(name)
        except:
            raise forms.ValidationError('Name is required')
        return name

    def clean_username(self):
        username = self.cleaned_data['username']
        validator = MinLengthValidator(1)
        try:
            validator(username)
        except:
            raise forms.ValidationError('User Name is required')
        return username

    def clean_qualification(self):
        qualification = self.cleaned_data['qualification']
        validator = MinLengthValidator(1)
        try:
            validator(qualification)
        except:
            raise forms.ValidationError('qualification is required')
        return qualification

    def clean_password(self):
        password = self.cleaned_data['password']
        validator = MinLengthValidator(8)
        try:
            validator(password)
        except:
            raise forms.ValidationError('Minimum length required fro password is 8')
        return password

