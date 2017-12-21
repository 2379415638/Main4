from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from . import forms
from . import models
from django.core.mail import send_mail
from random import randint
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import datetime
# Create your views here.
def check(request):
    try:
        usermail = request.session['usermail']
    except:
        usermail = None
    return usermail
def index(request):
    usermail = check(request)
    context = {'usermail':usermail}
    return render(request,'index.html',context)
def email(request,usermail):
    form = forms.Userform()
    response = ""
    if models.User.objects.filter(usermail = usermail).exists():
        response = "用户已存在.."
    else:
        form = forms.Userform(data = {'usermail':usermail})
        identify = randint(1000,9999)
        request.session['identify'] = identify
        body = "欢迎注册CodeUp\n验证码："+ str(identify)+"请勿告诉他人.."
        send_mail('CodeUp',body,'postmaster@seeksrq.top',[usermail,],fail_silently=False)
        response = "验证码已发送"
    context = {'usermail':check(request),'response':response,'form':form}
    return render(request,'user.html',context)
def user(request):
    response = ""
    usermail = check(request)
    if request.method == "POST":
        form = forms.Userform(data = request.POST)
        if form.is_valid():
            if request.session['identify'] == int(request.POST['identify']):
                user = models.User.objects.create(usermail = form.cleaned_data['usermail'],userpass = form.cleaned_data['userpass'],username = form.cleaned_data['username'])
                request.session['usermail'] = user.usermail
                request.session['userpass'] = user.userpass
                return HttpResponseRedirect(reverse("Formal:index"))
            else:
                response = "验证码错误"
    else:
        form = forms.Userform()
    context = {'form':form,'response':response,'usermail':usermail}
    return render(request, 'user.html', context)
def login(request):
    str = ""
    key = CaptchaStore.generate_key()
    print(key)
    image = captcha_image_url(key)
    print(image)
    usermail = check(request)
    if request.method == "POST":
        usercheckmail = request.POST['usermail']
        form = forms.Login(request.POST)
        if form.is_valid():
            if models.User.objects.filter(usermail = usercheckmail).exists():
                if models.User.objects.get(usermail = usercheckmail).userpass == form.cleaned_data['userpass']:
                    request.session['usermail'] =  usercheckmail
                    request.session['userpass'] = form.cleaned_data['userpass']
                    return HttpResponseRedirect(reverse("Formal:index"))
            str = "账号密码错误"
    else:
        form = forms.Login()
    context ={'form':form,'str':str,'usermail':usermail,'key':key,'image':image}
    return render(request,'login.html',context)
def logout(request):
    request.session.delete()
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def advice(request):
    usermail = check(request)
    context = {'usermail':usermail}
    return render(request, 'Advice.html',context)