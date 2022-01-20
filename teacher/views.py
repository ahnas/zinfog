from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model,login  as auth_login,logout as auth_logout
from django.shortcuts import render
from django.shortcuts import redirect
from student.models import Teacher, User
from student.views import studentlogin  
from .models import *
from student.models import *
# Create your views here.
def login(request):
    if request.POST:
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            auth_login(request,user)
            return redirect('teacher:dashboard')
        context={
        "is_teacherlogin":True,
        "error":"Invalid User name or password",
        
        }

    context={
        "is_teacherlogin":True,
        
    }
    return render(request,'pages/login.html',context)


def register(request):
    if request.POST:
        email = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        department = request.POST['department']
        Phone = request.POST['phone']

        get_user_model().objects.create_superuser(email,password)

        user=User.objects.get(email=email)
        teacher = Teacher()
        teacher.user=user
        teacher.name=name
        teacher.department=department
        teacher.phone=Phone
        teacher.save()
        return redirect('/teacher')


    context={
        "is_teacherRegister":True,
    }
    return render(request,'pages/registerteacher.html',context)

@login_required(login_url='teacher:login')
def adminDashboard(request):
    students=Student.objects.all()
    context={
        "students":students
    }
    return render(request,'pages/teacherDashboard.html',context)


def studentedit(request,id):
    student=Student.objects.get(id=id)
    context={
        "student":student,
        "is_studentedit":True
    }
    if request.POST:
        student=Student.objects.get(id=id)
        student.mark1=request.POST["m1"]
        student.mark2=request.POST["m2"]
        student.mark3=request.POST["m3"]
        student.save()
        success="Record Updated"
        context["success"]=success
    
    return render(request,'pages/studentEdit.html',context)