
from django.urls import path,include

from .views import *
from django.conf.urls.static import static


app_name='teacher'

urlpatterns = [ 
    path('', login,name="login"), 
    path('register', register,name="register"),
    path('dashboard', adminDashboard,name="dashboard"),
]