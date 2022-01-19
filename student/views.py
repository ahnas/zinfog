from django.shortcuts import render

# Create your views here.
def studentlogin(request):

    context={
        "is_studentlogin":True,
    }

    return render(request,'pages/login.html',context)


def register(request):
    
    context={
        "is_studentRegister":True,
    }
    return render(request,'pages/register.html',context)