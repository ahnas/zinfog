from pyexpat import model
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django import forms
from django.db.models.fields import DateField, SlugField
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create Save a User"""
        if not email:
            raise ValueError('User must have a Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user

    def create_superuser(self, email, password):
        """Create and Save a super User"""
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):
    """"Custom Model"""
    email = models.EmailField(max_length=225, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)


class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    department=models.CharField(max_length=225)
    phone=models.CharField(max_length=10)

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    dob=DateField()
    phone=models.CharField(max_length=30)
    image = VersatileImageField(blank=True,null=True,upload_to="Profile/",ppoi_field='image_ppoi')
    image_ppoi = PPOIField()
    mark1=models.IntegerField(default=0,blank=True,null=True)
    mark2=models.IntegerField(default=0,blank=True,null=True)
    mark3=models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return str(self.name)