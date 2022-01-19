
from django.shortcuts import render  

# Create your views here.
def login(request):
    context={
        "is_teacherlogin":True,
    }
    return render(request,'pages/login.html',context)


def register(request):

    context={
        "is_teacherRegister":True,
    }
    return render(request,'pages/registerteacher.html',context)

def adminDashboard(request):

    return render(request,'pages/teacherDashboard.html')