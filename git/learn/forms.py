from django import forms
from . import models
from captcha.fields import CaptchaField
class Login(forms.Form):
    usermail = forms.CharField(max_length = 20,required = True)
    userpass = forms.CharField(widget = forms.PasswordInput())
    captcha = CaptchaField()
class Userform(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username','usermail','userpass','enabled',]
        widgets = {'userpass':forms.PasswordInput}
        id = {'usermail':'usermail',}