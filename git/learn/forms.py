from django import forms
from captcha.fields import CaptchaField
class Login(forms.Form):
    usermail = forms.CharField(widget = forms.TextInput(attrs ={'placeholder':'邮箱'}))
    userpass = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'密码'}))
    captcha = CaptchaField()
class Userform(forms.Form):
    usermail = forms.EmailField(widget=forms.TextInput(attrs={'id':'usermail','placeholder':"邮箱"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username','placeholder':"姓名"}))
    userpass = forms.CharField(widget=forms.PasswordInput(attrs={'id':'userpass','placeholder':"密码"}))