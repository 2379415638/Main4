from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from . import models
from django.core.mail import send_mail
from random import randint
import datetime
#from django.HttpResponse import
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
        identify = randint(1000,9999)
        request.session['identify'] = identify
        body = "欢迎注册CodeUp\n验证码："+ str(identify)+"请勿告诉他人.."
        send_mail('CodeUp',body,'postmaster@seeksrq.top',[usermail,],fail_silently=False)
        response = "验证码已发送"
    context = {'form':form,'inputmail':usermail,'response':response}
    return render(request,'user.html',context)
def user(request):
    response = ""
    usermail = check(request)
    if request.method == "POST":
        form = forms.Userform(data = request.POST)
        if form.is_valid():
            if request.session['identify'] == int(request.POST['identify']):
                user = form.save(commit = 0)
                user.usermail = request.POST['usermail']
                user.save()
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
    if request.method == "POST":
        usermail = request.POST['usermail']
        form = forms.Login(request.POST)
        if form.is_valid():
            if models.User.objects.filter(usermail = usermail).exists():
                if models.User.objects.get(usermail = usermail).userpass == form.cleaned_data['userpass']:
                    request.session['usermail'] =  usermail
                    request.session['userpass'] = form.cleaned_data['userpass']
                    return HttpResponseRedirect(reverse("Formal:index"))
        str = "账号或密码错误"
        usermail = None
    else:
        usermail = None
        form = forms.Login()
    context ={'form':form,'str':str,'usermail':usermail}
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