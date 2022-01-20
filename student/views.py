
from pty import STDOUT_FILENO
import re
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login  as auth_login,logout as auth_logout
from .models import *

import imp
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login  as auth_login,logout as auth_logout
from django.shortcuts import redirect
from student.models import Teacher, User
from student.forms import StudentRegForm
import json
from django.http import HttpResponse




# Create your views here.
def studentlogin(request):
    

    context={
        "is_studentlogin":True,
    }

    return render(request,'pages/login.html',context)


def register(request):

    if request.POST:
        email = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo=request.FILES['photo']
        get_user_model().objects.create_user(email,password)
        user=User.objects.get(email=email)
        student=Student()
        student.user=user
        student.name=name
        student.dob=dob
        student.phone=phone
        student.image=photo
        student.save()
    context={
        "is_studentRegister":True,
    }

    return render(request,'pages/register.html',context)