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
    def _create_user(self, email, password,is_admin=False,is_active=False,
                     **extra_fields):
        """
        Método base para la creación de nuevos usuarios.
        """
        if not email:
            raise ValueError('The given email address must be set.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_admin=is_admin,
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
        return self._create_user(email, password,False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario marcándolo como super usuario.
        """
        return self._create_user(email, password,**extra_fields)


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
    mother_last_name=models.TextField(
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
    gender = models.TextField(max_length=50,blank=True)
    phone = models.TextField(
        max_length=20,
        blank=False,
        null=False
        )
    type_advisor= models.ForeignKey(Types_Advisors,blank=True, null=True)
    immovable_name = models.TextField(max_length=250,blank=True)
    immovable_phone = models.TextField(max_length=20,blank=True)
    photo = models.TextField(max_length=100,blank=True)
    register_date= models.DateField(auto_now_add=True)   
    permit_handbag = models.BooleanField(default=False)
    permit_diary = models.BooleanField(default=False)
    permit_notary = models.BooleanField(default=False)
    permit_broker = models.BooleanField(default=False)
    permit_proficient = models.BooleanField(default=False)
    permit_events = models.BooleanField(default=False)
    permit_documents = models.BooleanField(default=False)
    is_admin = models.BooleanField(
        default=False,
        verbose_name=_('is_admin')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is_active')
    )
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    'name',
    'last_name',
    'is_admin',
    'is_active',
    'phone'
    ]

class Countries(models.Model):
    name = models.TextField(max_length=100)
  

class States(models.Model):
    name = models.TextField(max_length=100)
    country = models.ForeignKey(Countries)

class Towns(models.Model):
    name = models.TextField(max_length=100)
    state = models.ForeignKey(States)

class Coins(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Immovables(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Publications(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Providers(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Contacts(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Events(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Types_Documents(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Providers(models.Model):
    name = models.TextField(max_length=100)
    type_provider= models.ForeignKey(Types_Providers)
    town= models.ForeignKey(Towns)
    register_date= models.DateField(auto_now_add=True)
    location= models.TextField(max_length=100)
    address= models.TextField(max_length=250)
    phone = models.TextField(max_length=20)
    email = models.EmailField(max_length=50)
    web_page = models.URLField(max_length=200)
    status = models.BooleanField(default=True)

class Classification_Providers(models.Model):
    score = models.IntegerField()
    user= models.ForeignKey(Users)
    provider=models.ForeignKey(Providers)

class Publications(models.Model):
    canvas_number = models.IntegerField(null=True)
    user= models.ForeignKey(Users,null=False)
    type_publications= models.ForeignKey(Types_Publications,null=False)
    type_immovable= models.ForeignKey(Types_Immovables,null=True)
    town= models.ForeignKey(Towns,null=False)
    location=models.TextField(max_length=200,null=False)
    title=models.TextField(max_length=100,null=False)
    description=models.TextField(max_length=500,null=False)
    price_first=models.DecimalField(decimal_places=2,max_digits=10,null=False)
    price_second=models.DecimalField(decimal_places=2,max_digits=10,null=True)
    coin=models.ForeignKey(Coins,null=False)
    old=models.IntegerField(null=True)
    bathrooms=models.IntegerField(null=True)
    ground_surface=models.TextField(max_length=50,null=True)
    construction_area=models.TextField(max_length=50,null=True)
    country=models.ForeignKey(Countries,null=False)
    state=models.ForeignKey(States,null=False)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Comments(models.Model):
    publication= models.ForeignKey(Publications)
    user= models.ForeignKey(Users)
    comment= models.TextField(max_length=1000)
    date= models.DateField(auto_now_add=True)

class Contacts(models.Model):
    name= models.TextField(max_length=100)
    lastname= models.TextField(max_length=100)
    phone= models.TextField(max_length=20)
    email = models.EmailField(max_length=50)
    user= models.ForeignKey(Users)
    type_contact= models.ForeignKey(Types_Contacts)
    note = models.TextField(max_length=200)

class Documents(models.Model):
    name= models.TextField(max_length=100)
    administrator=models.ForeignKey(Users)
    type_document= models.ForeignKey(Types_Documents)
    path=models.TextField(max_length=100)

class Events(models.Model):
    name= models.TextField(max_length=200)
    description= models.TextField(max_length=1000)
    administrator=models.ForeignKey(Users)
    type_event=models.ForeignKey(Types_Events)
    state=models.ForeignKey(States)
    town=models.ForeignKey(Towns)
    path=models.TextField(max_length=100)

class Favorites(models.Model):
    publication=models.ForeignKey(Publications)
    user= models.ForeignKey(Users)
    status = models.BooleanField(default=False)

class Notifications(models.Model):
    publication=models.ForeignKey(Publications)
    user= models.ForeignKey(Users)
    message= models.TextField(max_length=200)
    date= models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

class Push_Notifications(models.Model):
    publication=models.ForeignKey(Publications)
    user= models.ForeignKey(Users)
    device_token= models.TextField(max_length=200)
    device= models.TextField(max_length=20)
    status = models.BooleanField(default=True)
    date= models.DateField(auto_now_add=True)

class Favorites_Providers(models.Model):
    user=models.ForeignKey(Users)
    provider=models.ForeignKey(Providers)

class Photos(models.Model):
    name=models.TextField(max_length=60)
    path=models.TextField(max_length=100)
    publication=models.ForeignKey(Publications)

class Types_Reports(models.Model):
    name=models.TextField(max_length=60)
    status=models.BooleanField(default=True)

class Reports(models.Model):
    user=models.ForeignKey(Users)
    type_report=models.ForeignKey(Types_Reports)
    message=models.TextField(max_length=500)
    date= models.DateField(auto_now_add=True)
    
class User_Ubication(models.Model):
    user=models.ForeignKey(Users)
    country=models.ForeignKey(Countries)
    state=models.ForeignKey(States)
    date= models.DateField(auto_now_add=True)

class Types_Customers(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)

class Customers(models.Model):
    name= models.TextField(max_length=50)
    last_name= models.TextField(max_length=50,blank=False,null=False)
    mother_last_name=models.TextField(max_length=50,blank=True,null=True)
    phone= models.TextField(max_length=0)
    email= models.EmailField(max_length=100)
    contact=models.ForeignKey(Contacts)
    type_customer=models.ForeignKey(Types_Customers)

class Favorites_Customers(models.Model):
    customer=models.ForeignKey(Customers)
    user= models.ForeignKey(Users)

class Tasks(models.Model):
    description= models.TextField(max_length=300)
    date= models.DateField(auto_now_add=True)
    hour= models.TimeField(auto_now=False, auto_now_add=False)
    contact=models.ForeignKey(Contacts)
    user= models.ForeignKey(Users)

class Terms(models.Model):
    text= models.TextField(max_length=800)
    date= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    



            
            
            
            
            