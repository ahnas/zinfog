
from django.urls import path,include

from .views import *
from django.conf.urls.static import static


app_name='student' 

urlpatterns = [ 
    path('', studentlogin,name="studentlogin"), 
    path('register', register,name="register"), 
    path('studentDashboard', studentDashboard,name="studentDashboard"), 
    path('editstudent', editstudent,name="editstudent"), 
]