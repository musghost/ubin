# -*- encoding: utf-8 -*-
from .models import *
from .serializers import *

from rest_framework import serializers
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from rest_framework import filters
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.contrib.auth import login as auth_login
from django.db.models import Q
from rest_framework import status
from django.conf import settings
import hashlib
import os
import random
import string
import base64
from django.utils.encoding import smart_str
from django.db.models import Avg
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

import mimetypes
from django.http import StreamingHttpResponse
from django.core.servers.basehttp import FileWrapper
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.header import Header
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer, RefreshJSONWebTokenSerializer)
from rest_framework_jwt.settings import api_settings
from calendar import timegm
from datetime import datetime
from datetime import timedelta

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.renderers import JSONRenderer


'''
-----------  Country --------------------------
'''


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(CountryViewSet, self).get_permissions()

'''
-----------  State --------------------------
'''


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(StateViewSet, self).get_permissions()

'''
-----------  Town --------------------------
'''


class TownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    queryset = Town.objects.all()
    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TownViewSet, self).get_permissions()


'''
-----------  Neighborhood --------------------------
'''


class NeighborhoodViewSet(viewsets.ModelViewSet):
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(NeighborhoodViewSet, self).get_permissions()


class NeighborhoodFilterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = NeighborhoodFullSerializer
    queryset = Neighborhood.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'town__id'
    )


class TownFilterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TownFullSerializer
    queryset = Town.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'state__id'
    )


class StateFilterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = StateFullSerializer
    queryset = State.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'country__id'
    )

'''
-----------  Currencies --------------------------
'''


class CurrenciesViewSet(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(CurrenciesViewSet, self).get_permissions()


class vwCurrenciesViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Currencies.objects.all()
        serializer = CurrenciesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Currencies.objects.all()
        currency = get_object_or_404(queryset, pk=pk)
        serializer = CurrenciesSerializer(currency)

        return Response(serializer.data)


'''
-----------  Types Property --------------------------
'''


class TypesPropertyViewSet(viewsets.ModelViewSet):
    serializer_class = TypesPropertySerializer
    queryset = Types_Property.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesPropertyViewSet, self).get_permissions()


class vwTypesPropertyViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Property.objects.all()
        serializer = TypesPropertySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Property.objects.all()
        type_immovable = get_object_or_404(queryset, pk=pk)
        serializer = TypesPropertySerializer(type_immovable)

        return Response(serializer.data)


'''
-----------  Types Publications --------------------------
'''


class TypesPublicationsViewSet(viewsets.ModelViewSet):
    serializer_class = TypesPublicationsSerializer
    queryset = Types_Publications.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesPublicationsViewSet, self).get_permissions()


class vwTypesPublicationsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Publications.objects.all()
        serializer = TypesPublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Publications.objects.all()
        type_publication = get_object_or_404(queryset, pk=pk)
        serializer = TypesPublicationsSerializer(type_publication)

        return Response(serializer.data)

'''
-----------  Types Publications Past Due --------------------------
'''


class TypesPublicationsPastDueViewSet(viewsets.ModelViewSet):
    serializer_class = TypesPublicationsPastDueSerializer
    queryset = Types_Publications_Past_Due.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesPublicationsPastDueViewSet, self).get_permissions()

'''
-----------  Legal Status --------------------------
'''


class LegalStatusViewSet(viewsets.ModelViewSet):
    serializer_class = LegalStatusSerializer
    queryset = Legal_Status.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(LegalStatusViewSet, self).get_permissions()

'''
----------- Types Advisor --------------------------
'''


class TypesAdvisorsViewSet(viewsets.ModelViewSet):
    serializer_class = TypesAdvisorsSerializer
    queryset = Types_Advisors.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesAdvisorsViewSet, self).get_permissions()


class vwTypesAdvisorsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Advisors.objects.all()
        serializer = TypesAdvisorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Advisors.objects.all()
        type_advisor = get_object_or_404(queryset, pk=pk)
        serializer = TypesAdvisorsSerializer(type_advisor)

        return Response(serializer.data)


'''
----------- Types providers --------------------------
'''


class TypesProvidersViewSet(viewsets.ModelViewSet):
    serializer_class = TypesProvidersSerializer
    queryset = Types_Providers.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesProvidersViewSet, self).get_permissions()


class vwTypesProvidersViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Providers.objects.all()
        serializer = TypesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Providers.objects.all()
        type_provider = get_object_or_404(queryset, pk=pk)
        serializer = TypesProvidersSerializer(type_provider)

        return Response(serializer.data)


'''
------------- Types Events ----------------------
'''


class TypesEventsViewSet(viewsets.ModelViewSet):
    serializer_class = TypesEventsSerializer
    queryset = Types_Events.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesEventsViewSet, self).get_permissions()


class vwTypesEventsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Events.objects.all()
        serializer = TypesEventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Events.objects.all()
        type_event = get_object_or_404(queryset, pk=pk)
        serializer = TypesEventsSerializer(type_event)

        return Response(serializer.data)


'''
------------------ Types Documents -----------------
'''


class TypesDocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = TypesDocumentsSerializer
    queryset = Types_Documents.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesDocumentsViewSet, self).get_permissions()


class vwTypesDocumentsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Documents.objects.all()
        serializer = TypesDocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Documents.objects.all()
        type_document = get_object_or_404(queryset, pk=pk)
        serializer = TypesDocumentsSerializer(type_document)

        return Response(serializer.data)


'''
----------------  Register users -------------------------
'''


class RegisterViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, format=None):
        """
        Register user.
        ---
        type:
          photo:
            required: false
            type: file
          device_os:
            required: true
            type: string
          device_token:
            required: true
            type: string

        serializer: RegisterSerializer
        omit_serializer: false

        parameters:
            - name: photo
              description: Photo user.
              required: false
              type: file
              paramType: file
            - name: device_os
              description: device_os.
              equired: true
              paramType: form
            - name: device_token
              description: device_token.
              required: false
              paramType: form


        responseMessages:
            - code: 400
              message: BAD REQUEST
            - code: 200
              message: OK
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        photo = ""
        if len(request.FILES.items()) > 0:
            for key, file in request.FILES.items():
                randomtext = "".join(
                    [random.choice(string.digits + string.letters) for i in xrange(200)])
                hash_object = hashlib.sha1(randomtext)
                code = hash_object.hexdigest()
                file_name = hash_object.hexdigest()
                fileExtension = os.path.splitext(file.name)[1]
                photo = file_name + fileExtension
                path = settings.MEDIA_ROOT + file_name + fileExtension
                dest = open(path.encode('utf-8'), 'wb+')
                if file.multiple_chunks:
                    for c in file.chunks():
                        dest.write(c)
                else:
                    dest.write(file.read())
                    dest.close()

        request.POST = request.POST.copy()
        request.POST['photo'] = photo
        request.POST['is_active'] = True
        serializer = UsersSerializer(data=request.POST)

        if serializer.is_valid():

            user = serializer.save()

            # Save device
            request.data['user'] = user.id
            device_serializer = DevicesUserRegisterSerializer(
                data=request.data)
            if device_serializer.is_valid():
                device_serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
----------------  Get Token -------------------------
'''


class GetTokenViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, format=None):
        """
        Login
        ---

        type:
          email:
            required: true
            type: string
          password:
            required: true
            type: string
          device_os:
            required: true
            type: string
          device_token:
            required: false
            type: string

        parameters:
            - name: email
              description: email user.
              required: true
              type: string
              paramType: form
            - name: password
              description: Password.
              required: true
              type: string
              paramType: form
            - name: device_os
              required: true
              description: Mobile operating system device user.
              type: string
              paramType: form
            - name: device_token
              description: Device token.
              required: false
              type: string
              paramType: form

        responseMessages:
            - code: 400
              message: BAD REQUEST
            - code: 200
              message: OK
            - code: 500
              message: INTERNAL SERVER ERROR

        consumes:
            - application/json
        produces:
            - application/json
        """

        login_serializer = LoginSerializer(data=request.data)

        if login_serializer.is_valid():

            # Init user object.
            user = None

            try:

                # Get user.
                user = Users.objects.get(
                    email=request.data['email'],
                    is_active=True
                )

                # Check password.
                if not user.check_password(request.data['password']):

                    return Response(
                        {"non_field_errors": "Unable to login with provided credentials."},
                        status=status.HTTP_400_BAD_REQUEST)

            except Exception:
                return Response(
                    {"non_field_errors": "Unable to login with provided credentials."},
                    status=status.HTTP_400_BAD_REQUEST)

            # Save device
            request.data['user'] = user.id
            device_serializer = DevicesUserRegisterSerializer(
                data=request.data)
            if device_serializer.is_valid():
                device_serializer.save()

            # Generate Token.
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)

            if api_settings.JWT_ALLOW_REFRESH:
                payload['orig_iat'] = timegm(
                    datetime.utcnow().utctimetuple()
                )

            # Token.
            token = jwt_encode_handler(payload)
            user_serializer = UsersFullSerializer(user)

            return Response({"token": token, "user": user_serializer.data},
                            status=status.HTTP_200_OK
                            )

        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
----------------  Users -------------------------
'''


class UsersViewSet(viewsets.ViewSet):

    def list(self, request):
        permission_classes = (IsAdminUser,)
        queryset = Users.objects.all()
        serializer = UsersFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
            Register user
            ---
            type:
              photo:
                required: false
                type: file

            request_serializer: UsersSerializer
            response_serializer: UsersFullSerializer
            omit_serializer: false

            parameters_strategy: merge

            parameters:
               - name: photo
                 description: photo.
                 required: true
                 type: file
                 paramType: file

            responseMessages:
                - code: 400
                  message: BAD REQUEST
                - code: 200
                  message: OK
                - code: 201
                  message: CREATED
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        permission_classes = (IsAdminUser,)
        photo = ""
        for key, file in request.FILES.items():
            randomtext = "".join(
                [random.choice(string.digits + string.letters) for i in xrange(200)])
            hash_object = hashlib.sha1(randomtext)
            file_name = hash_object.hexdigest()
            fileExtension = os.path.splitext(file.name)[1]
            path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
            dest = open(path.encode('utf-8'), 'wb+')
            hash_name = file_name + fileExtension
            photo = hash_name
            path = settings.MEDIA_ROOT
            if file.multiple_chunks:
                for c in file.chunks():
                    dest.write(c)
            else:
                dest.write(file.read())
            dest.close()
        request.data['photo'] = photo
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(UsersFullSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        permission_classes = (IsAdminUser,)
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersFullSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
            Partial update user
            ---
            type:
              photo:
                required: false
                type: file

            request_serializer: UsersSerializer
            response_serializer: UsersFullSerializer
            omit_serializer: false

            parameters_strategy: merge
            parameters:
               - name: photo
                 description: photo.
                 required: true
                 type: file
                 paramType: file

            responseMessages:
                - code: 400
                  message: BAD REQUEST
                - code: 200
                  message: OK
                - code: 201
                  message: CREATED
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        user = get_object_or_404(Users, pk=pk)
        photo = user.photo
        if len(request.FILES.items()) > 0:
            file_path = settings.MEDIA_ROOT + str(photo)
            if os.path.isfile(file_path):
                os.remove(file_path)
            for key, file in request.FILES.items():
                randomtext = "".join(
                    [random.choice(string.digits + string.letters) for i in xrange(200)])
                hash_object = hashlib.sha1(randomtext)
                file_name = hash_object.hexdigest()
                fileExtension = os.path.splitext(file.name)[1]
                path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
                dest = open(path.encode('utf-8'), 'wb+')
                hash_name = file_name + fileExtension
                photo = hash_name
                if file.multiple_chunks:
                    for c in file.chunks():
                        dest.write(c)
                else:
                    dest.write(file.read())
                    dest.close()
        request.data['photo'] = photo
        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            if 'password' in request.data:
                user.set_password(request.data['password'])
                user.save()
            return Response(UsersFullSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        permission_classes = (IsAdminUser,)
        user = get_object_or_404(Users, pk=pk)
        file_path = settings.MEDIA_ROOT + str(user.photo)
        if os.path.isfile(file_path):
            os.remove(file_path)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentsFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DocumentsFullSerializer
    queryset = Documents.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'hash_name',
        'original_name',
        'path',
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'original_name',
        'hash_name',
        'administrator__id',
        'type_document__id',
        'path',
        'country__id',
        'state__id',
        'town__id',
        'status'
    )

    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class UsersFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UsersFullSerializer
    queryset = Users.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'email',
        'name',
        'last_name',
        'mothers_maiden_name',
        'birthday',
        'gender',
        'phone',
        'property_company_name',
        'property_company_phone',
        'photo'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'email',
        'name',
        'last_name',
        'mothers_maiden_name',
        'birthday',
        'gender',
        'phone',
        'type_advisor',
        'property_company_name',
        'property_company_phone',
        'photo',
        'allow_providers',
        'allow_notary',
        'allow_appraisers',
        'allow_past_due_portfolio',
        'allow_events',
        'allow_documents',
        'allow_diary',
        'allow_mortgage_broker',
        'is_superuser',
        'is_staff',
        'register_date',
        'is_active'
    )


class vwUsersViewSet(viewsets.ViewSet):

    def list(self, request):
        permission_classes = (IsAdminUser,)
        queryset = Users.objects.all()
        serializer = UsersDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        permission_classes = (IsAdminUser,)
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersDetailSerializer(user)
        return Response(serializer.data)


class AdvisorUsersViewSet(viewsets.ViewSet):

    def list(self, request, typeAdvisor_pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk
        )

        serializer = UsersDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typeAdvisor_pk=None, pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk
        )
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersDetailSerializer(user)
        return Response(serializer.data)


'''
----------------- Providers -----------------------
'''


class ProvidersViewSet(viewsets.ModelViewSet):

    serializer_class = ProvidersSerializer
    queryset = Providers.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(ProvidersViewSet, self).get_permissions()


class ProvidersDefaultFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProvidersFullSerializer
    queryset = Providers.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name',
        'address',
        'phone',
        'email',
        'web_page'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'type_provider__id',
        'state__id',
        'town__id',
        'neighborhood__id',
        'register_date',
        'address',
        'phone',
        'email',
        'web_page',
        'status',
        'is_favorite',
        'administrator__id'
    )


class vwProvidersTypeViewSet(viewsets.ViewSet):

    def list(self, request, typeProvider_pk=None):
        queryset = Providers.objects.filter(
            type_provider__pk=typeProvider_pk
        )

        serializer = ProvidersFullSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, typeProvider_pk=None, pk=None):
        queryset = Providers.objects.filter(
            type_provider__pk=provider_pk
        )
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersFullSerializer(provider)

        return Response(serializer.data)


class vwProvidersViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Providers.objects.all()
        serializer = ProvidersFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Providers.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersFullSerializer(provider)

        return Response(serializer.data)


'''
---------------- Calssifications Providers ---------------------
'''


class ClassificationProvidersViewSet(viewsets.ModelViewSet):

    serializer_class = ClassificationProvidersSerializer
    queryset = Classification_Providers.objects.all()


class vwClassificationProvidersViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk
        )

        serializer = ClassificationProvidersFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk
        )
        classificationPro = get_object_or_404(queryset, pk=pk)
        serializer = ClassificationProvidersFullSerializer(classificationPro)

        return Response(serializer.data)


class vwProviderClassificationProvidersViewSet(viewsets.ViewSet):

    def list(self, request, provider_pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk
        )

        serializer = ClassificationProvidersFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, provider_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk
        )
        classificationPro = get_object_or_404(queryset, pk=pk)
        serializer = ClassificationProvidersFullSerializer(classificationPro)

        return Response(serializer.data)


'''
---------------- Publications ----------------------
'''


class PublicationsViewSet(viewsets.ViewSet):

    def list(self, request):
        """
        Publication.
        ---

        request_serializer: PublicationsSerializer
        response_serializer: PublicationsFullSerializer
        omit_serializer: false  

        responseMessages:
          - code: 400
            message: BAD REQUEST
          - code: 200
            message: OK
          - code: 500
            message: INTERNAL SERVER ERROR
        consumes:
          - application/json
        produces:
          - application/json

        """
        queryset = Publications.objects.all()
        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Publication.
        ---

        type:
          photos_1:
            required: false
            type: file
          photo_2:
            required: false
            type: file
          photo_3:
            required: false
            type: file
          photo_4:
            required: false
            type: file
          photo_5:
            required: false
            type: file
          photo_6:
            required: false
            type: file

        request_serializer: PublicationsSerializer
        response_serializer: PublicationsFullSerializer
        omit_serializer: false

        parameters_strategy: merge
        parameters:
          - name: photo_1
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_2
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_3
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_4
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_5
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_6
            description: Photo publication.
            required: false
            type: file
            paramType: file    

        responseMessages:
          - code: 400
            message: BAD REQUEST
          - code: 200
            message: OK
          - code: 500
            message: INTERNAL SERVER ERROR
        consumes:
          - application/json
        produces:
          - application/json

        """
        serializer = PublicationsSerializer(data=request.POST)
        if serializer.is_valid():
            publication = serializer.save()
            if request.FILES.items():
                for key, file in request.FILES.items():
                    randomtext = "".join(
                        [random.choice(string.digits + string.letters) for i in xrange(200)])
                    hash_object = hashlib.sha1(randomtext)
                    code = hash_object.hexdigest()
                    file_name = hash_object.hexdigest()
                    fileExtension = os.path.splitext(file.name)[1]
                    photo = file_name + fileExtension
                    Photos(
                        hash_name=file_name + fileExtension,
                        original_name=file.name,
                        path=settings.MEDIA_ROOT,
                        publication=publication
                    ).save()
                    path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
                    dest = open(path.encode('utf-8'), 'wb+')
                    if file.multiple_chunks:
                        for c in file.chunks():
                            dest.write(c)
                    else:
                        dest.write(file.read())
                    dest.close()
            return Response(PublicationsFullSerializer(publication).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        permission_classes = (AllowAny,)
        queryset = Publications.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
        Publication.
        ---

        type:
          photos_1:
            required: false
            type: file
          photo_2:
            required: false
            type: file
          photo_3:
            required: false
            type: file
          photo_4:
            required: false
            type: file
          photo_5:
            required: false
            type: file
          photo_6:
            required: false
            type: file

        request_serializer: PublicationsSerializer
        response_serializer: PublicationsFullSerializer
        omit_serializer: false

        parameters_strategy: merge
        parameters:
          - name: photo_1
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_2
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_3
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_4
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_5
            description: Photo publication.
            required: false
            type: file
            paramType: file
          - name: photo_6
            description: Photo publication.
            required: false
            type: file
            paramType: file    

        responseMessages:
          - code: 400
            message: BAD REQUEST
          - code: 200
            message: OK
          - code: 500
            message: INTERNAL SERVER ERROR
        consumes:
          - application/json
        produces:
          - application/json

        """
        publication = get_object_or_404(Publications, pk=pk)
        if len(request.FILES.items()) > 0:
            for key, file in request.FILES.items():
                randomtext = "".join(
                    [random.choice(string.digits + string.letters) for i in xrange(200)])
                hash_object = hashlib.sha1(randomtext)
                code = hash_object.hexdigest()
                file_name = hash_object.hexdigest()
                fileExtension = os.path.splitext(file.name)[1]
                id_photo = os.path.splitext(file.name)[0]
                photo = None
                try:
                    id_photo = int(id_photo)
                    photo = Photos.objects.get(pk=id_photo)
                except Exception:
                    photo = None

                if photo:
                    file_path = settings.MEDIA_ROOT + photo.hash_name
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    photo.hash_name = file_name + fileExtension
                    photo.save()
                    path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
                    dest = open(path.encode('utf-8'), 'wb+')
                    if file.multiple_chunks:
                        for c in file.chunks():
                            dest.write(c)
                        else:
                            dest.write(file.read())
                        dest.close()
                else:
                    path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
                    dest = open(path.encode('utf-8'), 'wb+')
                    if file.multiple_chunks:
                        for c in file.chunks():
                            dest.write(c)
                        else:
                            dest.write(file.read())
                        dest.close()
                    Photos(
                        hash_name=file_name + fileExtension,
                        original_name=file.name,
                        path=settings.MEDIA_ROOT,
                        publication=publication
                    ).save()

        serializer = PublicationsSerializer(
            publication, data=request.data, partial=True)
        if serializer.is_valid():
            publication = serializer.save()
            return Response(PublicationsFullSerializer(publication).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        publication = get_object_or_404(Publications, pk=pk)
        for photo in publication.photos.all():
            file_path = settings.MEDIA_ROOT + photo.hash_name
            Photos.objects.get(pk=photo.id).delete()
            if os.path.isfile(file_path):
                os.remove(file_path)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicationsDefaultFilterViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PublicationsFullSerializer
    queryset = Publications.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'description',
        'title'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'user__id',
        'user__type_advisor__id',
        'canvas_number',
        'type_publications__id',
        'type_publications_past_due__id',
        'type_property__id',
        'title',
        'price_first',
        'currency__id',
        'bathrooms',
        'antiquity',
        'area',
        'construction_area',
        'country__id',
        'state__id',
        'town__id',
        'neighborhood__id',
        'mortgage',
        'price_appraisal',
        'legal_status',
        'date',
        'code',
        'status'
    )

    def get_queryset(self):
        from_price = self.request.query_params.get('from_price', None)
        to_price = self.request.query_params.get('to_price', None)
        if from_price is not None and to_price is not None:
            return Publications.objects.filter(
                price_first__range=(from_price, to_price)
            )
        return Publications.objects.all()


class vwPublicationsInTypeImmovableViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, typeProperty_pk=None):
        queryset = Publications.objects.filter(
            type_property__pk=typeProperty_pk
        )

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typeProperty_pk=None, pk=None):
        queryset = Publications.objects.filter(
            type_property__pk=typeProperty_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)


class vwPublicationsInTypePublicationViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, typePublication_pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk
        )

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typePublication_pk=None, pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)


class vwPublicationsCurrenciesViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, currency_pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk
        )

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, currency_pk=None, pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)


class vwPublicationsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, user_pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk
        )

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)


class vwAllPublicationsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = Publications.objects.all()

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Publications.objects.all()
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)


'''
------------------ Comments ------------------------
'''


class CommentsViewSet(viewsets.ModelViewSet):

    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class CommentsFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CommentsFullerializer
    queryset = Comments.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'comment'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'publication__id',
        'user__id',
        'comment',
        'date',
        'status'
    )


class vwCommentsViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Comments.objects.filter(
            user__pk=user_pk
        )

        serializer = CommentsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Comments.objects.filter(
            user__pk=user_pk
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsFullSerializer(comment)
        return Response(serializer.data)


class vwCommentsPublicationsViewSet(viewsets.ViewSet):

    def list(self, request, publication_pk=None):
        queryset = Comments.objects.filter(
            publication__pk=publication_pk
        )

        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, publication_pk=None, pk=None):
        queryset = Comments.objects.filter(
            publication__pk=user_pk
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)


'''
--------------- Documents ---------------------
'''


class DocumentsViewSet(viewsets.ViewSet):

    def list(self, request):
        permission_classes = (IsAuthenticated,)
        queryset = Documents.objects.all()
        serializer = DocumentsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
            Documents Insert, original_name should be input name in your form,
            send enctype multipart.
            ---
            type:
              original_name:
                required: true
                type: file
              hash_name:
                required: false
                type: string
              path:
                required: false
                type: string

            request_serializer: DocumentsSerializer
            response_serializer: DocumentsSerializer
            omit_serializer: false

            parameters_strategy: merge
            omit_parameters:
               - hash_name
            parameters:
               - name: original_name
                 description: Document.
                 required: true
                 type: file
                 paramType: file
               - name: hash_name
                 required: false
                 type: string
                 paramType: form
               - name: path
                 required: false
                 type: string
                 paramType: form

            responseMessages:
                - code: 400
                  message: BAD REQUEST
                - code: 200
                  message: OK
                - code: 201
                  message: CREATED
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        permission_classes = (IsAdminUser,)
        hash_name = ""
        path = ""
        for key, file in request.FILES.items():
            randomtext = "".join(
                [random.choice(string.digits + string.letters) for i in xrange(200)])
            hash_object = hashlib.sha1(randomtext)
            file_name = hash_object.hexdigest()
            fileExtension = os.path.splitext(file.name)[1]
            path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
            dest = open(path.encode('utf-8'), 'wb+')
            hash_name = file_name + fileExtension
            path = settings.MEDIA_ROOT
            if file.multiple_chunks:
                for c in file.chunks():
                    dest.write(c)
            else:
                dest.write(file.read())
            dest.close()
        request.data['hash_name'] = hash_name
        request.data['path'] = path
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Documents.objects.all()
        document = get_object_or_404(queryset, pk=pk)
        serializer = DocumentsFullSerializer(document)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
            Documents partial update, it's not necesary send all mandatory parameters.
            ---
            type:
              original_name:
                required: true
                type: file
              hash_name:
                required: false
                type: string
              path:
                required: false
                type: string

            request_serializer: DocumentsSerializer
            response_serializer: DocumentsSerializer
            omit_serializer: false

            parameters_strategy: merge
            omit_parameters:
               - hash_name
            parameters:
               - name: original_name
                 description: Document.
                 required: true
                 type: file
                 paramType: file
               - name: hash_name
                 required: false
                 type: string
                 paramType: form
               - name: path
                 required: false
                 type: string
                 paramType: form

            responseMessages:
                - code: 400
                  message: BAD REQUEST
                - code: 200
                  message: OK
                - code: 201
                  message: CREATED
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        permission_classes = (IsAdminUser,)
        document = get_object_or_404(Documents, pk=pk)
        hash_name = document.hash_name
        path = document.path
        original_name = document.original_name
        if len(request.FILES.items()) > 0:
            file_path = settings.MEDIA_ROOT + str(document.hash_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
            for key, file in request.FILES.items():
                randomtext = "".join(
                    [random.choice(string.digits + string.letters) for i in xrange(200)])
                hash_object = hashlib.sha1(randomtext)
                file_name = hash_object.hexdigest()
                fileExtension = os.path.splitext(file.name)[1]
                path = settings.MEDIA_ROOT + file_name + fileExtension  # file.name
                dest = open(path.encode('utf-8'), 'wb+')
                hash_name = file_name + fileExtension
                original_name = file.name
                path = settings.MEDIA_ROOT
                if file.multiple_chunks:
                    for c in file.chunks():
                        dest.write(c)
                else:
                    dest.write(file.read())
                    dest.close()
        request.data['hash_name'] = hash_name
        request.data['path'] = path
        request.data['original_name'] = original_name
        serializer = DocumentsSerializer(
            document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        permission_classes = (IsAdminUser,)
        document = get_object_or_404(Documents, pk=pk)
        file_path = settings.MEDIA_ROOT + str(document.hash_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentsFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = DocumentsFullSerializer
    queryset = Documents.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'hash_name',
        'original_name',
        'path',
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'original_name',
        'hash_name',
        'administrator__id',
        'type_document',
        'path',
        'country__id',
        'state__id',
        'town__id',
        'status'
    )


class DocumentsTypeViewSet(viewsets.ViewSet):

    def list(self, request, typeDocument_pk=None):
        permission_classes
        queryset = Documents.objects.filter(
            type_document__pk=typeDocument_pk
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typeDocument_pk=None, pk=None):
        queryset = Documents.objects.filter(
            type_document__pk=typeDocument_pk
        )
        document = get_object_or_404(queryset, pk=pk)
        serializer = DocumentsSerializer(document)
        return Response(serializer.data)


class vwDocumentsViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Documents.objects.filter(
            administrator__pk=user_pk
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Documents.objects.filter(
            administrator__pk=user_pk
        )
        document = get_object_or_404(queryset, pk=pk)
        serializer = DocumentsSerializer(document)
        return Response(serializer.data)


'''
-------------- Events --------------------------
'''


class EventsViewSet(viewsets.ModelViewSet):

    serializer_class = EventsSerializer
    queryset = Events.objects.all()


class EventsFilterViewSet(viewsets.ModelViewSet):
    serializer_class = EventsFullSerializer
    queryset = Events.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name',
        'description',
        'address'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'address',
        'description',
        'type_event',
        'date_event',
        'hour',
        'administrator__id',
        'status'
    )


'''
-------------- Favorites -------------------------
'''


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


class UnfavoriteViewSet(viewsets.ViewSet):

    def create(self, request):
        """
            Unfavorite publication.
            ---

            request_serializer: FavoritesSerializer
            response_serializer: FavoritesSerializer
            omit_serializer: false

            responseMessages:
                - code: 204
                  message: NO CONTENT
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        favorite = Favorites.objects.filter(
            publication__id=request.data['publication'],
            user__id=request.data['user']
        )
        if favorite:
            favorite.delete()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritesFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = FavoritesFullSerializer
    queryset = Favorites.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    filter_fields = ('id', 'publication__id', 'user__id', 'status')


class vwFavoritesPublicationsViewSet(viewsets.ViewSet):

    def list(self, request, publication_pk=None):
        queryset = Favorites.objects.filter(
            publication__pk=publication_pk
        )

        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, publication_pk=None, pk=None):
        queryset = Favorites.bjects.filter(
            publication__pk=publication_pk
        )
        favorite = get_object_or_404(queryset, pk=pk)
        serializer = FavoritesSerializer(favorite)
        return Response(serializer.data)


'''
------------------ Notifications ----------------------
'''


class NotificationsViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationsSerializer
    queryset = Notifications.objects.all()


class NotificationsFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = NotificationsFullSerializer
    queryset = Notifications.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'publication__id',
        'task__id',
        'user__id',
        'message',
        'date',
        'read',
        'type_notification',
        'status'
    )

    def get_queryset(self):
        if self.request.user.id:
            return Notifications.objects.filter(
                Q(publication__user__id=self.request.user.id, type_notification=1) |
                Q(task__user__id=self.request.user.id, type_notification=2) |
                Q(user__id=self.request.user.id, type_notification=3)
            )
        return Notifications.objects.filter(pk=0)


class vwNotificationsViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Notifications.objects.filter(
            user__pk=user_pk
        )

        serializer = NotificationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            user__pk=user_pk
        )
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationsFullSerializer(notification)
        return Response(serializer.data)


class vwNotificationsPublicationsViewSet(viewsets.ViewSet):

    def list(self, request, publication_pk=None):
        queryset = Notifications.objects.filter(
            publication__pk=publication_pk
        )

        serializer = NotificationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, publication_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            publication__pk=user_pk
        )
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationsFullSerializer(notification)
        return Response(serializer.data)


'''
----------------- Push Notifications  -----------------
'''


class PushNotificationsViewSet(viewsets.ModelViewSet):

    serializer_class = PushNotificationsSerializer
    queryset = Push_Notifications.objects.all()


class vwPushNotificationsViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Push_Notifications.objects.filter(
            user__pk=user_pk
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Push_Notifications.bjects.filter(
            user__pk=user_pk
        )
        push_notification = get_object_or_404(queryset, pk=pk)
        serializer = PushNotificationsSerializer(push_notification)
        return Response(serializer.data)


class vwPushNotificationsPubViewSet(viewsets.ViewSet):

    def list(self, request, publication_pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, publication_pk=None, pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk
        )
        push_notification = get_object_or_404(queryset, pk=pk)
        serializer = PushNotificationsSerializer(push_notification)
        return Response(serializer.data)

'''
------------------- Photos ----------------------------
'''


class PhotosViewSet(viewsets.ModelViewSet):

    serializer_class = PhotosSerializer
    queryset = Photos.objects.all()


class PhotosDefaultFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PhotosFullSerializer
    queryset = Photos.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'hash_name',
        'original_name',
        'path',
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'hash_name',
        'original_name',
        'path',
        'status'
    )


class vwPhotosPublicationsViewSet(viewsets.ViewSet):

    def list(self, request, publication_pk=None):
        queryset = Photos.objects.filter(
            publication__pk=publication_pk
        )

        serializer = PhotosFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, publication_pk=None, pk=None):
        queryset = Photos.objects.filter(
            publication__pk=publication_pk
        )
        photo = get_object_or_404(queryset, pk=pk)
        serializer = PhotosFullSerializer(photo)
        return Response(serializer.data)

'''
----------------- Types Reports --------------------
'''


class TypesReportsViewSet(viewsets.ModelViewSet):
    serializer_class = TypesReportsSerializer
    queryset = Types_Reports.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypesReportsViewSet, self).get_permissions()


class vwAllTypesReportsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Reports.objects.all()
        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Reports.objects.all()
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)


'''
--------------- Reports ----------------------
'''


class ReportsViewSet(viewsets.ModelViewSet):

    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()


class vwReportsViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Reports.objects.filter(
            user__pk=user_pk
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Reports.objects.filter(
            user__pk=user_pk
        )
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)


class vwTypeReportsViewSet(viewsets.ViewSet):

    def list(self, request, typeReport_pk=None):
        queryset = Reports.objects.filter(
            type_report__pk=typeReport_pk
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typeReport_pk=None, pk=None):
        queryset = Reports.objects.filter(
            type_report__pk=typeReport_pk
        )
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)


'''
-------------- User Location ------------------------
'''


class UserLocationViewSet(viewsets.ModelViewSet):

    serializer_class = UserLocationSerializer
    queryset = User_Location.objects.all()


class vwUserLocationViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = User_Location.objects.filter(
            user__pk=user_pk
        )

        serializer = UserLocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = User_Location.objects.filter(
            user__pk=user_pk
        )
        user_u = get_object_or_404(queryset, pk=pk)
        serializer = UserLocationSerializer(user_u)
        return Response(serializer.data)

''''
----------------- Type Customers --------------------
'''


class TypeCustomersViewSet(viewsets.ModelViewSet):
    serializer_class = TypeCustomersSerializer
    queryset = Types_Customers.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(TypeCustomersViewSet, self).get_permissions()


class vwAllTypesCustomersViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Types_Customers.objects.all()
        serializer = TypeCustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Types_Customers.objects.all()
        type_customer = get_object_or_404(queryset, pk=pk)
        serializer = TypeCustomersSerializer(type_customer)
        return Response(serializer.data)

'''
--------------  Customers ----------------------
'''


class CustomersViewSet(viewsets.ModelViewSet):

    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()


class CustomersFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomersFullSerializer
    queryset = Customers.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'name',
        'last_name',
        'mothers_maiden_name',
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'name',
        'last_name',
        'mothers_maiden_name',
        'phone',
        'email',
        'user__id',
        'note',
        'type_customer',
        'is_favorite',
        'status'
    )


class vwCustomersForTypeViewSet(viewsets.ViewSet):

    def list(self, request, typeCustomer_pk=None):
        queryset = Customers.objects.filter(
            type_customer__pk=typeCustomer_pk
        )

        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, typeCustomer_pk=None, pk=None):
        queryset = Customers.objects.filter(
            type_customer__pk=typeCustomer_pk
        )
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomersSerializer(customer)
        return Response(serializer.data)


'''
--------------  Tasks ----------------------
'''


class TasksViewSet(viewsets.ModelViewSet):

    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()


class TasksFilterViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TasksFullSerializer
    queryset = Tasks.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'description'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'description',
        'date',
        'hour',
        'customer__id',
        'user__id',
        'status'
    )


class vwTasksViewSet(viewsets.ViewSet):

    def list(self, request, user_pk=None):
        queryset = Tasks.objects.filter(
            user__pk=user_pk
        )

        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user_pk=None, pk=None):
        queryset = Tasks.objects.filter(
            user__pk=user_pk
        )
        task = get_object_or_404(queryset, pk=pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)


'''-------------------- Device User Reigister -------------------------------------'''


class DevicesUserRegisterDefaultFilterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DevicesUserRegisterFullSerializer
    queryset = Devices_User_Register.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = (
        'device_name'
    )
    ordering_fields = '__all__'
    filter_fields = (
        'id',
        'device_user',
        'device_token',
        'device_os',
        'device_register_date',
        'device_status'
    )


class DevicesUserRegisterViewSet(viewsets.ModelViewSet):

    serializer_class = DevicesUserRegisterSerializer
    queryset = Devices_User_Register.objects.all()

'''-------------------- Recover password -------------------------------------'''


class RecoverPasswordViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, format=None):
        """
            Recover password.
            ---
            type:
              email:
                required: true
                type: string
            parameters:
                - name: email
                  description: Email user which try recover password.
                  required: true
                  type: string
                  paramType: form
            responseMessages:
                - code: 400
                  message: BAD REQUEST
                - code: 201
                  message: CREATED
                - code: 500
                  message: INTERNAL SERVER ERROR
            consumes:
                - application/json
            produces:
                - application/json
        """
        if 'email' in request.data:
            email = request.data['email']
            queryset = Users.objects.filter(email=email, is_active=True)
            user = get_object_or_404(queryset)
            randomtext = "".join(
                [random.choice(string.digits + string.letters) for i in xrange(5)])
            user.set_password(randomtext)
            user.save()
            serializer = UsersSerializer(user)
            try:
                password = randomtext
                name = serializer.data['name']
                body = 'Hola ' + name + u', tu contraseña es : ' + password
                subject = u'UBIN : Recuperar contraseña'
                subject = subject.encode("utf_8").decode("utf_8")
                body = body.encode("utf_8").decode("utf_8")
                send_mail(subject, body, 'web@administrator.com',
                          [email], fail_silently=False)
            except Exception as e:
                return Response({'message': 'The email could not be sent.', 'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'email': 'email is mandatory field.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': u'Se ha enviado la contraseña.', 'email': serializer.data['email']}, status=status.HTTP_200_OK)


class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        """
        Logout 
        ---
        responseMessages:
            - code: 201
              message: CREATED
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        try:
            if device_token in request.GET:
                device = Devices_User_Register.objects.get(
                    device_token=request.GET['device_token'])
                device.delete()
        except Exception, e:
            print "Error logout" + e

        logout(request)
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)
