

import re
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login  as auth_login,logout as auth_logout
from .models import *
from django.contrib.auth.decorators import login_required
import imp
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login  as auth_login,logout as auth_logout
from django.shortcuts import redirect
from student.models import Teacher, User
from student.forms import StudentRegForm
import json
from django.http import HttpResponse
from django.contrib import messages





# Create your views here.
def studentlogin(request):
    if request.POST:
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        
        if user:
            auth_login(request,user)
            return redirect('student:studentDashboard')
        else:
            messages.error(request, 'invalid Username or Password.')
            print("invalid Username Password")
        context={
            
        "is_studentlogin":True,
        "error":"Invalid User name or password",
        }

    context={
        "is_studentlogin":True,
    }

    return render(request,'pages/login.html',context)


@login_required(login_url='student:login')
def studentDashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    context={
        "student":student
    }
    return render(request,'pages/studentView.html',context)


@login_required(login_url='student:login')
def editstudent(request):
    

    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    context={
        "student":student
    }
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        dob=request.POST['dob']
        student = Student.objects.get(user=request.user)
        student.name=name
        student.phone=phone
        student.dob=dob
        student.save()
        return redirect('student:studentDashboard')
    return render(request,'pages/editstudent.html',context)
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
        response_data = {
                "status" : "true",
                "title" : "Successfully Registered",
                
            }
        
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    context={
        "is_studentRegister":True,
    }

    return render(request,'pages/register.html',context)