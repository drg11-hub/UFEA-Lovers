from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from Home.models import Cont_us
from django.contrib.auth.decorators import login_required
from django.conf import settings
import re

# Create your views here.

def Home(request):
    return render(request, 'Home/Home.html')

#@login_required(login_url="/log_in",redirect_field_name="/Home")
@login_required(login_url="/Login",redirect_field_name="/Home")
def Contact_us(request):
    if request.method=='POST':
        Full_name = request.POST['Full_name']
        email_addr = request.POST['email_addr']
        ph_no = request.POST['ph_no']
        Content = request.POST['Content']
        Contact_us = Cont_us(Full_name=Full_name, email_addr= email_addr, ph_no=ph_no, Content=Content)
        Contact_us.save()
        obj1=User.objects.get(email=email_addr)
        USER=obj1.username
        subject="UFEA"
        messaging = render_to_string('Home/Email_Cont_us.html',{'USER':USER})
        from_email=settings.EMAIL_HOST_USER
        email_to_send=EmailMessage(subject=subject, body=messaging, from_email=from_email, to=[email_addr])
        email_to_send.content_subtype = "html"
        email_to_send.send(fail_silently=False)
        messages.success(request, 'Response is Recorded.\nA mail regarding this has been sent to you.')
    return render(request, 'Home/Contact_us.html')

def About_us(request):
    return render(request, 'Home/About_us.html')

def log_in(request):
    if request.method == 'POST':
        Login_U_name=request.POST['Login_U_name']
        login_pwd=request.POST['login_pwd']
        #login_email=request.POST['login_email']
        user = authenticate(username=Login_U_name, password=login_pwd)
        print(Login_U_name)

        if user is not None:
            login(request, user)
            messages.success(request, f'Logged In Successfull.\nWelcome {Login_U_name}.')
            return redirect('Home')
        else:
            messages.error(request, 'Invalid Credentials provided.\nUnable to Login. Please Try again.')
            return redirect('Home')
    return HttpResponse('404 Not Found')

@login_required(login_url="{%  url 'log_in' %}")
def log_out(request):
    logout(request)
    messages.success(request, 'Successfully Logged-Out.')
    return redirect('Home')

def userProfile(request):
    return render(request, 'Home/Profile.html')

def handleSignup(request):
    if request.method == 'POST':
        F_name=request.POST['F_name']
        L_name=request.POST['L_name']
        Signup_U_name=request.POST['Signup_U_name']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        signup_email=request.POST['signup_email']
        contact=request.POST['contact']
        DOB=request.POST['DOB']
        gender=request.POST['gender']
        Status=request.POST['Status']

        if len(Signup_U_name)>15:
            messages.error(request, 'Username must be of maximum 15 characters.')
            return redirect('Home')
        if not Signup_U_name.isalnum():
            messages.error(request, 'Username must contain only Letters and Numbers (Alpha-numeric).')
            return redirect('Home')
        if pwd1 != pwd2:
            messages.error(request, 'Passwords Donot Match.')
            return redirect('Home')

        myuser=User.objects.create_user(Signup_U_name, signup_email, pwd1)
        myuser.first_name=F_name
        myuser.last_name=L_name
        myuser.cont=contact
        myuser.BD=DOB
        myuser.gend=gender
        myuser.stat=Status
        myuser.save()
        messages.success(request, 'Your Account has been Successfully Created!\nWe have sent you a mail.')
        subject="UFEA"
        messaging = render_to_string('Home/Signup_Email.html',{'USER':Signup_U_name})
        from_email=settings.EMAIL_HOST_USER
        email_to_send=EmailMessage(subject=subject, body=messaging, from_email=from_email, to=[signup_email])
        email_to_send.content_subtype = "html"
        email_to_send.send(fail_silently=False)
        return redirect('Home')
    else:
        return HttpResponse('404- Not Found')