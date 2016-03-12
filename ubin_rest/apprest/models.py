# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from django.core.mail import EmailMultiAlternatives



# Create your models here.

class Country(models.Model):
    name = models.TextField(
        max_length=60,
        null=False,
        blank=False
    )


class State(models.Model):
    name = models.TextField(
        max_length=200,
        null=False,
        blank=False
    )
    country = models.ForeignKey(Country, null=False, related_name='states')


class Town(models.Model):
    name = models.TextField(
        max_length=200,
        null=False,
        blank=False
    )
    state = models.ForeignKey(State, null=False, related_name='towns')

class Neighborhood(models.Model):
    name = models.TextField(
        max_length=200,
        null=False,
        blank=False
    )
    town = models.ForeignKey(Town, null=False, related_name='neighborhood')


class Types_Advisors(models.Model):
    name = models.TextField(max_length=100)
    status = models.BooleanField(default=True)


class UsuarioManager(BaseUserManager):
    """
    Manager personalizado para el modelo usuario.
    """

    def _create_user(self, email, password, is_superuser=False, is_staff=False, is_active=False,
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
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario marcándolo como super usuario.
        """
        return self._create_user(email, password, True, True, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    name = models.TextField(
        max_length=50,
        blank=False,
        null=False
    )
    last_name = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    mothers_maiden_name = models.TextField(
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
    type_advisor = models.ForeignKey(
        Types_Advisors, blank=True, null=True, related_name="user")
    property_company_name = models.TextField(max_length=250, blank=True)
    property_company_phone = models.TextField(max_length=20, blank=True)
    photo = models.TextField(max_length=250, blank=True)
    path_photo = models.TextField(max_length=250, blank=True)
    register_date = models.DateField(auto_now_add=True)
    allow_providers = models.BooleanField(default=False)
    allow_notary = models.BooleanField(default=False)
    allow_appraisers = models.BooleanField(default=False)
    allow_past_due_portfolio = models.BooleanField(default=False)
    allow_events = models.BooleanField(default=False)
    allow_documents = models.BooleanField(default=False)
    allow_diary = models.BooleanField(default=False)
    allow_mortgage_broker = models.BooleanField(default=False)
    is_staff = models.BooleanField(
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

    def get_full_name(self):
        """
        Return full name user:
             name last_name mothers_maiden_name
        """
        parts = [self.name, self.last_name, self.mothers_maiden_name]
        return ' '.join(filter(None, parts))

    def get_short_name(self):
        """
        Return short name user:
            name last_name
        """
        parts = [self.name, self.last_name]
        return ' '.join(filter(None, parts))

    def email_user(self, subject, txt, html=None, from_email=None, **kwargs):
        """
        Send email to user.
        """
        if not from_email :
            from_email = settings.DEFAULT_FROM_EMAIL

        message = EmailMultiAlternatives(
            subject, txt, from_email, [self.email], **kwargs)

        if html is not None:
            message.attach_alternative(html, 'text/html')

        message.send()


class Currencies(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    symbol = models.TextField(max_length=2, null=False, blank=False)
    code = models.TextField(max_length=3, null=False, blank=False)
    value = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    status = models.BooleanField(default=True, null=False, blank=False)


class Types_Property(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Types_Publications(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Types_Publications_Past_Due(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Types_Providers(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Types_Events(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Types_Documents(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Legal_Status(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Providers(models.Model):
    name = models.TextField(max_length=100)
    type_provider = models.ForeignKey(Types_Providers, null=False)
    state = models.ForeignKey(
        State, null=True, related_name='providers_in_state')
    town = models.ForeignKey(Town, null=True, related_name='providers_in_town')
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, related_name='providers_in_neighborhood')
    references = models.TextField(max_length=100)
    register_date = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=250)
    phone = models.TextField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    web_page = models.URLField(max_length=200)
    is_favorite = models.BooleanField(default=False)
    administrator = models.ForeignKey(
        Users, null=False, related_name="providers")
    status = models.BooleanField(default=True)


class Classification_Providers(models.Model):
    score = models.IntegerField(null=False)
    user = models.ForeignKey(Users, null=False)
    provider = models.ForeignKey(Providers, null=False, related_name="score")
    status = models.BooleanField(default=True)


class Publications(models.Model):
    canvas_number = models.IntegerField(null=True)
    user = models.ForeignKey(Users, null=False, related_name="user")
    type_publications = models.ForeignKey(Types_Publications, null=True)
    type_publications_past_due = models.ForeignKey(
        Types_Publications_Past_Due,
        null=True
    )
    type_property = models.ForeignKey(Types_Property, null=True)
    title = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=False)
    price_first = models.DecimalField(
        decimal_places=2, max_digits=50, null=False)
    currency = models.ForeignKey(Currencies, null=False)
    bathrooms = models.FloatField(null=True)
    antiquity = models.FloatField(null=True)
    area = models.IntegerField(null=False)
    construction_area = models.IntegerField(null=False)
    country = models.ForeignKey(
        Country, null=True, related_name='publications_in_country')
    state = models.ForeignKey(
        State, null=True, related_name='publications_in_state')
    town = models.ForeignKey(
        Town, null=True, related_name='publications_in_town')
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, related_name='publications_in_neighborhood')
    date = models.DateTimeField(auto_now_add=False, auto_now=False, null=False)
    code = models.TextField(max_length=50, null=True, blank=True)
    mortgage = models.IntegerField(default=1, null=True)
    price_appraisal = models.DecimalField(
        decimal_places=2, max_digits=50, null=True)
    legal_status = models.ForeignKey(Legal_Status, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['date', 'price_first']


class Comments(models.Model):
    publication = models.ForeignKey(
        Publications, null=False, related_name='comments')
    user = models.ForeignKey(Users, null=False)
    comment = models.TextField(max_length=1000, null=False, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    status = models.BooleanField(default=True)


def after_insert_comment(sender, instance, **kwargs):
    Notifications(
        message=instance.comment,
        publication=instance.publication,
        task=None,
        user=instance.user,
        date=instance.date,
        read=False,
        type_notification=1,
        status=True
    ).save()

# register the signal
post_save.connect(after_insert_comment, sender=Comments, dispatch_uid=__file__)


class Documents(models.Model):
    original_name = models.TextField(max_length=250, null=False, blank=False)
    hash_name = models.TextField(max_length=250, null=False, blank=False)
    administrator = models.ForeignKey(Users, null=False)
    type_document = models.ForeignKey(Types_Documents, null=False)
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(
        State, null=True, related_name='documents_in_state')
    town = models.ForeignKey(Town, null=True, related_name='documents_in_town')
    path = models.TextField(max_length=100, null=False)
    status = models.BooleanField(default=True)


class Events(models.Model):
    name = models.TextField(max_length=200, null=False, blank=False)
    address = models.TextField(max_length=300, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.TextField(max_length=100, null=False, blank=False)
    type_event = models.ForeignKey(Types_Events, null=False)
    date_event = models.DateField(
        auto_now_add=False, null=False, editable=True)
    hour = models.TimeField(null=False)
    administrator = models.ForeignKey(Users, null=False)
    status = models.BooleanField(default=True)
    town = models.ForeignKey(Town, null=True, related_name='events_in_town')


class Favorites(models.Model):
    publication = models.ForeignKey(
        Publications, null=False, related_name='favorite')
    user = models.ForeignKey(Users, null=False, related_name="favorite")
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = ("publication", "user")

    class Meta:
        unique_together = ("publication", "user")


class Push_Notifications(models.Model):
    publication = models.ForeignKey(Publications, null=False)
    user = models.ForeignKey(Users, null=False)
    device_token = models.TextField(max_length=200, null=False, blank=False)
    device = models.TextField(max_length=20, null=False, blank=False)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)


class Photos(models.Model):
    hash_name = models.TextField(max_length=250, null=False, blank=False)
    original_name = models.TextField(max_length=250, null=False, blank=False)
    path = models.TextField(max_length=250, null=False, blank=False)
    publication = models.ForeignKey(
        Publications, null=False, related_name="photos")
    status = models.BooleanField(default=True)


class Types_Reports(models.Model):
    name = models.TextField(max_length=60, null=False, blank=False)
    status = models.BooleanField(default=True)


class Reports(models.Model):
    user = models.ForeignKey(Users, null=False)
    type_report = models.ForeignKey(Types_Reports, null=False)
    message = models.TextField(max_length=500, null=False, blank=False)
    date = models.DateField(
        auto_now_add=False, auto_now=False, null=False, editable=True)
    status = models.BooleanField(default=True)


class User_Location(models.Model):
    user = models.ForeignKey(Users, null=False)
    country = models.ForeignKey(Country, null=True)
    state = models.ForeignKey(State, null=True)
    town = models.ForeignKey(Town, null=True)
    neighborhood = models.ForeignKey(Neighborhood, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


class Types_Customers(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


class Customers(models.Model):
    name = models.TextField(max_length=50, blank=False, null=False)
    last_name = models.TextField(max_length=50, blank=False, null=False)
    mothers_maiden_name = models.TextField(
        max_length=50, blank=True, null=True)
    phone = models.TextField(max_length=0, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    type_customer = models.ForeignKey(Types_Customers, null=False)
    user = models.ForeignKey(Users, null=False, related_name="customers")
    note = models.TextField(max_length=200, null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    status = models.BooleanField(default=True)


class Tasks(models.Model):
    description = models.TextField(max_length=300, null=False, blank=False)
    date = models.DateField(
        auto_now_add=False, auto_now=False, null=False, editable=True)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    customer = models.ForeignKey(Customers, null=True)
    user = models.ForeignKey(Users, null=False)
    status = models.BooleanField(default=True)


def after_insert_task(sender, instance, **kwargs):
    Notifications(
        message=instance.description,
        publication=None,
        task=instance,
        user=instance.user,
        date=instance.date,
        read=False,
        type_notification=2,
        status=True
    ).save()

# register the signal
post_save.connect(after_insert_task, sender=Tasks, dispatch_uid=__file__)


class Notifications(models.Model):
    publication = models.ForeignKey(Publications, null=True)
    task = models.ForeignKey(Tasks, null=True)
    user = models.ForeignKey(Users, null=False)
    message = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=False, null=False)
    read = models.BooleanField(default=False)
    type_notification = models.IntegerField(null=True)
    status = models.BooleanField(default=True)


class Devices_User_Register(models.Model):
    device_user = models.ForeignKey(Users, null=False)
    device_os = models.TextField(max_length=30, null=False, blank=False)
    device_token = models.TextField(max_length=300, null=True, blank=True)
    device_register_date = models.DateField(auto_now_add=True)
    device_status = models.BooleanField(default=True)

    class Meta:
        unique_together = ("device_user", "device_token")
