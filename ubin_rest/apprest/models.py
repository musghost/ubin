# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Types_Advisors(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class UsuarioManager(BaseUserManager):
    """
    Manager personalizado para el modelo usuario.
    """
    def _create_user(self, email, password,is_superuser=False,is_staff=False,is_active=False,
                     **extra_fields):
        """
        Método base para la creación de nuevos usuarios.
        """
        if not email:
            raise ValueError('The given email address must be set.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario.
        """
        return self._create_user(email, password,False,False,**extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario marcándolo como super usuario.
        """
        return self._create_user(email, password,True,True,**extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    name = models.TextField(
        max_length=50,
        blank=False,
        null=False
        )
    last_name = models.TextField(
        max_length=100, 
        blank=False,
        null=False,
        )
    mothers_maiden_name=models.TextField(
        max_length=50,
        blank=True,
        null=True
        )
    email = models.EmailField(
        max_length=100,
        unique=True,
        null=False
        )
    birthday = models.DateField(null=True)
    gender = models.TextField(
        max_length=50,
        blank=True,
        null=True)
    phone = models.TextField(
        max_length=20,
        blank=False,
        null=False
        )
    type_advisor= models.ForeignKey(Types_Advisors,blank=True, null=True)
    property_company_name = models.TextField(max_length=250,blank=True)
    property_company_phone = models.TextField(max_length=20,blank=True)
    photo = models.TextField(max_length=250,blank=True)
    path_photo =models.TextField(max_length=250,blank=True)
    register_date= models.DateField(auto_now_add=True) 
    allow_providers = models.BooleanField(default=False) 
    allow_notary = models.BooleanField(default=False) 
    allow_appraisers = models.BooleanField(default=False)
    allow_past_due_portfolio = models.BooleanField(default=False)
    allow_events = models.BooleanField(default=False)
    allow_documents = models.BooleanField(default=False)
    allow_diary = models.BooleanField(default=False)
    allow_mortgage_broker = models.BooleanField(default=False)
    is_staff= models.BooleanField(
        default=False,
        verbose_name=_('is_staff')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is_active')
    )
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    'name',
    'phone',
    'is_active'
    ]

class Currencies(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Property(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Publications(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Providers(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Contacts(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Events(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Types_Documents(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Providers(models.Model):
    name = models.TextField(max_length=100)
    type_provider= models.ForeignKey(Types_Providers,null=False)
    state=models.IntegerField(null=False)
    town=models.IntegerField(null=False)
    neighborhood=models.IntegerField(null=False)
    register_date= models.DateField(auto_now_add=True)
    address= models.TextField(max_length=250)
    phone = models.TextField(max_length=20,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    web_page = models.URLField(max_length=200)
    status = models.BooleanField(default=True)


class Classification_Providers(models.Model):
    score = models.IntegerField(null=False)
    user= models.ForeignKey(Users,null=False)
    provider=models.ForeignKey(Providers,null=False,related_name="score")
    status = models.BooleanField(default=True)

class Publications(models.Model):
    canvas_number = models.IntegerField(null=True)
    user= models.ForeignKey(Users,null=False)
    type_publications= models.ForeignKey(Types_Publications,null=False)
    type_property= models.ForeignKey(Types_Property,null=True)
    title=models.TextField(max_length=100,null=False)
    description=models.TextField(max_length=500,null=False)
    price_first=models.DecimalField(decimal_places=2,max_digits=10,null=False)
    price_second=models.DecimalField(decimal_places=2,max_digits=10,null=True)
    currency=models.ForeignKey(Currencies,null=False)
    bathrooms=models.IntegerField(null=True)
    antiquity=models.TextField(max_length=50,null=True)
    area=models.TextField(max_length=50,null=True)
    construction_area=models.TextField(max_length=50,null=True)
    country=models.IntegerField(null=False)
    state=models.IntegerField(null=False)
    town=models.IntegerField(null=False)
    neighborhood=models.IntegerField(null=False)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Comments(models.Model):
    publication= models.ForeignKey(Publications,null=False)
    user= models.ForeignKey(Users,null=False)
    comment= models.TextField(max_length=1000,null=False,blank=False)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

class Contacts(models.Model):
    name= models.TextField(max_length=100,null=False,blank=False)
    lastname= models.TextField(max_length=100,null=False,blank=False)
    mothers_maiden_name=models.TextField(max_length=50,blank=True,null=True)
    phone= models.TextField(max_length=20,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    user= models.ForeignKey(Users,null=False)
    type_contact= models.ForeignKey(Types_Contacts,null=False)
    note = models.TextField(max_length=200)
    is_favorite=models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Documents(models.Model):
    original_name= models.TextField(max_length=250,null=False,blank=False)
    hash_name=models.TextField(max_length=250,null=False,blank=False)
    administrator=models.ForeignKey(Users,null=False)
    type_document= models.ForeignKey(Types_Documents,null=False)
    path=models.TextField(max_length=100,null=False)
    status = models.BooleanField(default=True)

class Events(models.Model):
    name= models.TextField(max_length=200,null=False,blank=False)
    description= models.TextField(max_length=1000,null=False,blank=False)
    type_event=models.ForeignKey(Types_Events,null=False)
    date_event=models.DateField(auto_now_add=True)
    administrator=models.ForeignKey(Users,null=False)
    status = models.BooleanField(default=True)

class Favorites(models.Model):
    publication=models.ForeignKey(Publications,null=False,related_name='favorite')
    user= models.ForeignKey(Users,null=False)
    status = models.BooleanField(default=False)


class Notifications(models.Model):
    publication=models.ForeignKey(Publications,null=False)
    user= models.ForeignKey(Users,null=False)
    message= models.TextField(max_length=200,null=False,blank=False)
    date= models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Push_Notifications(models.Model):
    publication=models.ForeignKey(Publications,null=False)
    user= models.ForeignKey(Users,null=False)
    device_token= models.TextField(max_length=200,null=False,blank=False)
    device= models.TextField(max_length=20,null=False,blank=False)
    status = models.BooleanField(default=True)
    date= models.DateField(auto_now_add=True)

class Favorites_Providers(models.Model):
    user=models.ForeignKey(Users,null=False)
    provider=models.ForeignKey(Providers,null=False, related_name='favorite')
    status = models.BooleanField(default=True)

class Photos(models.Model):
    name=models.TextField(max_length=250,null=False,blank=False)
    path=models.TextField(max_length=250,null=False,blank=False)
    publication=models.ForeignKey(Publications,null=False)
    status = models.BooleanField(default=True)

class Types_Reports(models.Model):
    name=models.TextField(max_length=60,null=False,blank=False)
    status=models.BooleanField(default=True)

class Reports(models.Model):
    user=models.ForeignKey(Users,null=False)
    type_report=models.ForeignKey(Types_Reports,null=False)
    message=models.TextField(max_length=500,null=False,blank=False)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
class User_Location(models.Model):
    user=models.ForeignKey(Users,null=False)
    country=models.IntegerField(null=False)
    state=models.IntegerField(null=False)
    town=models.IntegerField(null=False)
    neighborhood=models.IntegerField(null=False)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

class Types_Customers(models.Model):
    name = models.TextField(max_length=100,null=False,blank=False)
    status = models.BooleanField(default=True)

class Customers(models.Model):
    name= models.TextField(max_length=50,blank=False,null=False)
    last_name= models.TextField(max_length=50,blank=False,null=False)
    mothers_maiden_name=models.TextField(max_length=50,blank=True,null=True)
    phone= models.TextField(max_length=0,blank=False,null=False)
    email= models.EmailField(max_length=100,blank=False,null=False)
    type_customer=models.ForeignKey(Types_Customers,null=False)
    status = models.BooleanField(default=True)

class Favorites_Customers(models.Model):
    customer=models.ForeignKey(Customers,null=False)
    user= models.ForeignKey(Users,null=False)
    status = models.BooleanField(default=True)

class Tasks(models.Model):
    description= models.TextField(max_length=300,null=False,blank=False)
    date= models.DateField(auto_now_add=True)
    hour= models.TimeField(auto_now=False, auto_now_add=False)
    contact=models.ForeignKey(Contacts)
    user= models.ForeignKey(Users,null=False)
    status = models.BooleanField(default=True)


    



            
            
            
            
            