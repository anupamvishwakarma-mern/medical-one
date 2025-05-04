from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class GenderChoices(object):
    UNKNOWN=0
    MALE=1
    FEMALE=2
    CHOICES = (
        (UNKNOWN, "Unknown"),
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

from datetime import datetime


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, password,mobile, first_name ):
        if  not mobile:
            raise ValueError('Users must have a mobile')

        user = self.model( mobile=mobile, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, mobile, first_name, password):
        user = self.create_user(
            password=password, mobile=mobile, first_name=first_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,BaseModel,PermissionsMixin):
    gender =  models.PositiveSmallIntegerField(choices=GenderChoices.CHOICES,default=GenderChoices.UNKNOWN)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.BigIntegerField("Mobile",unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = [ 'first_name','password']

    def __str__(self):
        return "{}:{}".format(self.mobile,self.first_name)
        
