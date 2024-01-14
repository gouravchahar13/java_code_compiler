from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField
from django import forms


class Signup_Form(UserCreationForm,forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class Login_form(forms.Form):
    captcha = ReCaptchaField()