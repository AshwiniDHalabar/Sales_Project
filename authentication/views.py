from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from authentication.models import Newuser
from django.contrib import messages
from django.shortcuts import redirect, render
from server import settings

# Create your views here.
def index(request):
    return render(request,'authentication/index.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name',False)
        last_name = request.POST.get('last_name',False)
        email = request.POST.get('email',False)
        password = request.POST.get('password',False)
        confirmpassword = request.POST.get('confirmpassword',False)
        phonenumber = request.POST.get('phonenumber',False)
        Newuser(first_name=first_name,last_name=last_name,email=email,password=password,confirmpassword=confirmpassword,phonenumber=phonenumber).save()
        return HttpResponse("<h1>User registration created SUCCESSFULLY</h1>")
    else:
        return render(request,'authentication/register.html')

def login(request):
    if request.method == 'POST':
        first_name = request.POST('first_name')
        passowrd = request.POST('password',False)
        return HttpResponse("<h4>login success</h4>")

    else:
        return render(request,'authentication/login.html')

def abc(request):
    pass
