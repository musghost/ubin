from .models import Currencies
from .models import Types_Property
from .models import Types_Publications
from .models import Types_Advisors
from .models import Types_Providers
from .models import Types_Advisors
from .models import Types_Providers
from .models import Types_Contacts
from .models import Types_Events
from .models import Types_Documents
from .models import Users
from .models import Providers
from .models import Classification_Providers
from .models import Publications
from .models import Comments
from .models import Contacts 
from .models import Documents
from .models import Events 
from .models import Favorites
from .models import Notifications
from .models import Push_Notifications
from .models import Favorites_Providers
from .models import Favorites_Providers
from .models import Photos
from .models import Types_Reports
from .models import Reports
from .models import User_Location
from .models import Types_Customers
from .models import Customers
from .models import Favorites_Customers
from .models import Tasks

from .serializers import CurrenciesSerializer
from .serializers import TypesPropertySerializer
from .serializers import TypesPublicationsSerializer
from .serializers import TypesAdvisorsSerializer
from .serializers import TypesProvidersSerializer
from .serializers import TypesContactsSerializer
from .serializers import TypesEventsSerializer
from .serializers import TypesDocumentsSerializer
from .serializers import UsersSerializer
from .serializers import ProvidersSerializer
from .serializers import ProvidersFullSerializer
from .serializers import ClassificationProvidersSerializer
from .serializers import PublicationsSerializer
from .serializers import PublicationsFullSerializer
from .serializers import CommentsSerializer
from .serializers import CommentsFullerializer
from .serializers import ContactsSerializer
from .serializers import DocumentsSerializer
from .serializers import EventsSerializer
from .serializers import FavoritesSerializer
from .serializers import NotificationsSerializer
from .serializers import PushNotificationsSerializer
from .serializers import FavoritesProvidersSerializer
from .serializers import PhotosSerializer
from .serializers import TypesReportsSerializer
from .serializers import ReportsSerializer
from .serializers import UserLocationSerializer
from .serializers import TypeCustomersSerializer
from .serializers import CustomersSerializer
from .serializers import FavoritesCustomersSerializer
from .serializers import TasksSerializer

from rest_framework import serializers
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from rest_framework import filters
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q

#from rest_framework_jwt.authentication import JSONWebTokenAuthentication


'''
-----------  Currencies --------------------------
'''
class CurrenciesViewSet(viewsets.ModelViewSet):
 
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()

class vwCurrenciesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Currencies.objects.filter(status=True)
        serializer = CurrenciesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Currencies.objects.filter(status=True)
        currency = get_object_or_404(queryset, pk=pk)
        serializer = CurrenciesSerializer(currency)

        return Response(serializer.data)


'''
-----------  Types Property --------------------------
'''

class TypesPropertyViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesPropertySerializer
    queryset = Types_Property.objects.all()

class vwTypesPropertyViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Property.objects.filter(status=True)
        serializer = TypesPropertySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Property.objects.filter(status=True)
        type_immovable = get_object_or_404(queryset, pk=pk)
        serializer = TypesPropertySerializer(type_immovable)

        return Response(serializer.data)


'''
-----------  Types Publications --------------------------
'''

class TypesPublicationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesPublicationsSerializer
    queryset = Types_Publications.objects.all()

class vwTypesPublicationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Publications.objects.filter(status=True)
        serializer = TypesPublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Publications.objects.filter(status=True)
        type_publication = get_object_or_404(queryset, pk=pk)
        serializer = TypesPublicationsSerializer(type_publication)

        return Response(serializer.data)

'''
----------- Types Advisor --------------------------
'''
class TypesAdvisorsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesAdvisorsSerializer
    queryset = Types_Advisors.objects.all()

class vwTypesAdvisorsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Advisors.objects.filter(status=True)
        serializer = TypesAdvisorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Advisors.objects.filter(status=True)
        type_advisor = get_object_or_404(queryset, pk=pk)
        serializer = TypesAdvisorsSerializer(type_advisor)

        return Response(serializer.data)


'''
----------- Types providers --------------------------
'''
class TypesProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesProvidersSerializer
    queryset = Types_Providers.objects.all()

class vwTypesProvidersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Providers.objects.filter(status=True)
        serializer = TypesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Providers.objects.filter(status=True)
        type_provider = get_object_or_404(queryset, pk=pk)
        serializer = TypesProvidersSerializer(type_provider)

        return Response(serializer.data)


'''
------------- Types Contacts ----------------------
'''
class TypesContactsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesContactsSerializer
    queryset = Types_Contacts.objects.all()

class vwTypesContactsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Contacts.objects.filter(status=True)
        serializer = TypesContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Contacts.objects.filter(status=True)
        type_contact = get_object_or_404(queryset, pk=pk)
        serializer = TypesContactsSerializer(type_contact)

        return Response(serializer.data)


'''
------------- Types Events ----------------------
'''
class TypesEventsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesEventsSerializer
    queryset = Types_Events.objects.all()

class vwTypesEventsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Events.objects.filter(status=True)
        serializer = TypesEventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Events.objects.filter(status=True)
        type_event = get_object_or_404(queryset, pk=pk)
        serializer = TypesEventsSerializer(type_event)

        return Response(serializer.data)



'''
------------------ Types Documents -----------------
'''
class TypesDocumentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesDocumentsSerializer
    queryset = Types_Documents.objects.all()

class vwTypesDocumentsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Documents.objects.filter(status=True)
        serializer = TypesDocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Documents.objects.filter(status=True)
        type_document = get_object_or_404(queryset, pk=pk)
        serializer = TypesDocumentsSerializer(type_document)

        return Response(serializer.data)



'''
----------------  Users -------------------------
'''
class UsersViewSet(viewsets.ModelViewSet):
 
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class vwUsersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Users.objects.filter(status=True)
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Users.objects.filter(status=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class AdvisorUsersViewSet(viewsets.ViewSet):
    def list(self, request,typeAdvisor_pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk, status=True
        )

        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeAdvisor_pk=None,pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk, status=True
        )
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)



'''
----------------- Providers -----------------------
'''
class ProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ProvidersSerializer
    queryset = Providers.objects.all()

class vwProvidersTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeProvider_pk=None):
        queryset = Providers.objects.filter(
            type_provider__pk=typeProvider_pk,status=True
        )

        serializer = ProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeProvider_pk=None, pk=None):
        queryset = Providers.objects.filter(
            type_provider__pk=provider_pk,status=True
        )
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersSerializer(provider)

        return Response(serializer.data)

class vwProvidersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Providers.objects.filter(status=True)
        serializer = ProvidersFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Providers.objects.filter(status=True)
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersFullSerializer(provider)

        return Response(serializer.data)

class ProvidersFilterListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset=Providers.objects.all() # Get all providers

        result_list=[] # Declare var result list empty
        if 'limit' in request.GET:
            count=queryset.count()
            if count > request.GET['limit']:
                queryset=Providers.objects.all()[:request.GET['limit']]
        if 'name' in request.GET:
            queryset=queryset.filter(name=request.GET['name'])
        if 'type_provider' in request.GET:
            if 'town' in request.GET:
                queryset=queryset.filter(
                    type_provider=request.GET['type_provider'],
                    town=request.GET['town']
                    )
            else:
                queryset=queryset.filter(type_provider=request.GET['type_provider'])
        if 'state' in request.GET:
            queryset.filter(state=request.GET['state'])
        if 'town' in request.GET:
            queryset=queryset.filter(town=request.GET['town'])
        if 'neighborhood' in request.GET:
            queryset=queryset.filter(neighborhood=request.GET['neighborhood'])
        if 'register_date' in request.GET:
            queryset=queryset.filter(register_date=request.GET['register_date'])
        if 'address' in request.GET:
            queryset=queryset.filter(address=request.GET['address'])
        if 'phone' in request.GET:
            queryset=queryset.filter(phone=request.GET['phone'])
        if 'email' in request.GET:
            queryset=queryset.filter(email=request.GET['email'])
        if 'web_page' in request.GET:
            queryset=queryset.filter(web_page=request.GET['web_page'])
        if 'status' in request.GET:
            queryset=queryset.filter(status=request.GET['status'])
        if 'like' in request.GET:
            like=request.GET['like']
            queryset=queryset.filter(
                Q(name__contains=like) 
                | Q(address__contains=like) 
                | Q(phone__contains=like) 
                | Q(email__contains=like) 
                | Q(web_page__contains=like)
            )
        if 'orderAsc' in request.GET:
            queryset=queryset.order_by(request.GET['orderAsc'])
        if 'orderDesc' in request.GET:
            queryset=queryset.order_by('-'+request.GET['orderAsc'])
        favorite_provider=Favorites_Providers.objects.all()
        classification_provider=Classification_Providers.objects.all()
        for provider in queryset:
            # this provider is favorite?
            favorite_provider=favorite_provider.filter(id=provider.id)
            favorite=False
            if favorite_provider:
                favorite=True
            # Validation provider in classification for get average score
            if 'user' in request.GET:
                classification_provider=classification_provider.filter(provider__pk=provider.id,user__pk=request.GET['user'])
            else:
                classification_provider=classification_provider.filter(provider__pk=provider.id)
            average=0
            if classification_provider:
                average=classification_provider.filter(provider__pk=provider.id).aggregate(Avg('score'))
            #Serialize provider
            type_provider_name=provider.type_provider.name
            provider=serializers.serialize('json',queryset.filter(id=provider.id))

            provider_json={
            'provider':provider,
            'type_provider_name':type_provider_name,
            'favorite':favorite,
            'average':average
            }

            result_list.append(provider_json)

        return HttpResponse(json.dumps(result_list))


'''
---------------- Calssifications Providers ---------------------
'''
class ClassificationProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ClassificationProvidersSerializer
    queryset = Classification_Providers.objects.all()

class vwClassificationProvidersViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk, status=True
        )

        serializer = ClassificationProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk,status=True
        )
        classificationPro = get_object_or_404(queryset, pk=pk)
        serializer = ClassificationProvidersSerializer(classificationPro)

        return Response(serializer.data)

class vwProviderClassificationProvidersViewSet(viewsets.ViewSet):
    def list(self, request,provider_pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk,status=True
        )

        serializer = ClassificationProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,provider_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk,status=True
        )
        classificationPro = get_object_or_404(queryset, pk=pk)
        serializer = ClassificationProvidersSerializer(classificationPro)

        return Response(serializer.data)


'''
---------------- Publications ----------------------
'''
class PublicationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = PublicationsSerializer
    queryset = Publications.objects.all()


class PublicationsFilterListViewSet(viewsets.ViewSet):
    def list(self, request):

        queryset=Publications.objects.all()# Get all publications
        if 'limit' in request.GET:
            count=queryset.count()
            if count > request.GET['limit']:
                queryset=Publications.objects.all()[:request.GET['limit']]
        
        result_list=[] # Declare var result list empty

        '''
        Apply filters
        '''
        if 'like' in request.GET:
            like=request.GET['like']
            queryset=queryset.filter(
                Q(title__contains=like)
                |Q(description__contains=like)
                |Q(description__contains=like)
                |Q(antiquity__contains=like)
                |Q(area__contains=like)
                |Q(construction_area__contains=like)
            )
        if 'canvas_number' in request.GET:
            queryset=queryset=queryset.filter(canvas_number=request.GET['canvas_number'])
        if 'type_publication' in request.GET:
            queryset=queryset=queryset.filter(type_publication=request.GET['type_publication'])
        if 'type_property' in request.GET:
            queryset=queryset=queryset.filter(type_property=request.GET['type_property'])
        if 'title' in request.GET:
            queryset=queryset=queryset.filter(title=request.GET['title'])
        if 'price_second' in request.GET:
            queryset=queryset=queryset.filter(price_second=request.GET['price_second'])
        if 'currency' in request.GET:
            queryset=queryset=queryset.filter(currency=request.GET['currency'])
        if 'bathrooms' in request.GET:
            queryset=queryset=queryset.filter(bathrooms=request.GET['bathrooms'])
        if 'antiquity' in request.GET:
            queryset=queryset=queryset.filter(antiquity=request.GET['antiquity'])
        if 'area' in request.GET:
            queryset=queryset=queryset.filter(area=request.GET['area'])
        if 'construction_area' in request.GET:
            queryset=queryset=queryset.filter(construction_area=request.GET['construction_area'])
        if 'country' in request.GET:
            queryset=queryset=queryset.filter(country=request.GET['country'])
        if 'state' in request.GET:
            queryset=queryset=queryset.filter(state=request.GET['state'])
        if  'town' in request.GET:
            queryset=queryset=queryset.filter(town=request.GET['town'])
        if  'neighborhood' in request.GET:
            queryset=queryset.filter(neighborhood=request.GET['neighborhood'])
        if 'user' in request.GET:
            queryset=queryset.filter(user=request.GET['user'])
        if 'advisor' in request.GET:
            queryset=queryset.filter(user__type_advisor=request.GET['advisor'])
        if 'price' in request.GET:
            queryset=queryset.filter(price_one=request.GET['price'])
        if 'date' in request.GET:
            queryset=queryset.filter(date=request.GET['date'])
        if 'status' in request.GET:
            queryset=queryset.filter(status=request.GET['status'])
        if 'orderAsc' in request.GET:
            queryset=queryset.order_by(request.GET['orderAsc'])
        if 'orderDesc' in request.GET:
            queryset=queryset.order_by("-"+request.GET['orderDesc'])

        favorite_publication_queryset=Favorites.objects.all()
        user_queryset=Users.objects.all()
        type_publication_queryset=Types_Publications.objects.all()
        type_property_queryset=Types_Property.objects.all()
        currency_queryset=Currencies.objects.all()
        type_advisor_queryset=Types_Advisors.objects.all()

        for publication in queryset:
            favorite_publication=favorite_publication_queryset.filter(publication=publication.id)
            favorite=False
            if favorite_publication :
                favorite=True
            type_publication=serializers.serialize('json',type_publication_queryset.filter(id=publication.type_publications.id))
            type_property=serializers.serialize('json',type_property_queryset.filter(id=publication.type_property.id))
            currency=serializers.serialize('json',currency_queryset.filter(id=publication.currency.id))
            user_queryset=user_queryset.filter(id=publication.user.id)
            type_advisor_id=0
            type_advisor_name=""
            if 'type_advisor' in user_queryset:
                type_advisor_queryset=type_advisor_queryset.filter(id=user_queryset.type_advisor.id)
                type_advisor_id=type_advisor_queryset.id
                type_advisor_name=type_advisor_queryset.name
            user=serializers.serialize('json',user_queryset)
            publication=serializers.serialize(
                'json',
                queryset.filter(id=publication.id),
                fields=(
                    'id',
                    'title',
                    'description',
                    'price_first',
                    'price_second',
                    'bathrooms',
                    'antiquity',
                    'area',
                    'construction_area',
                    'country',
                    'state',
                    'town',
                    'neighborhood',
                    'date',
                    'status')
                )

            publication_json={
            'publication':publication,
            'user':user,
            'type_advisor_id': type_advisor_id,
            'type_advisor_name':type_advisor_name,
            'type_publication':type_publication,
            'type_property':type_property,
            'currency':currency,
            'isfavorite':favorite,
            'votes':favorite_publication.count()
            }
            result_list.append(publication_json)

        return HttpResponse(json.dumps(result_list))

class vwPublicationsInTypeImmovableViewSet(viewsets.ViewSet):
    def list(self, request,typeProperty_pk=None):
        queryset = Publications.objects.filter(
            type_property__pk=typeProperty_pk,status=True
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeProperty_pk=None,pk=None):
        queryset = Publications.objects.filter(
            type_property__pk=typeProperty_pk,status=True
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsInTypePublicationViewSet(viewsets.ViewSet):
    def list(self, request,typePublication_pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk,status=True
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typePublication_pk=None,pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk,status=True
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsCurrenciesViewSet(viewsets.ViewSet):
    def list(self, request,currency_pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk,status=True
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,currency_pk=None,pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk,status=True
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk,status=True
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwAllPublicationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Publications.objects.filter(status=True)

        serializer = PublicationsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Publications.objects.filter(status=True)
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsFullSerializer(publication)
        return Response(serializer.data)




'''
------------------ Comments ------------------------
'''
class CommentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

class vwCommentsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Comments.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
        queryset = Comments.objects.filter(
            user__pk=user_pk,status=True
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

class vwCommentsPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Comments.objects.filter(
            publication__pk=publication_pk,status=True
        )

        serializer = CommentsFullerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,publication_pk=None,pk=None):
        queryset = Comments.objects.filter(
            publication__pk=user_pk,status=True
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsFullerializer(comment)
        return Response(serializer.data)



'''
----------------  Contacts ---------------------
'''
class ContactsViewSet(viewsets.ModelViewSet):
 
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class vwAllContactsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contacts.objects.filter(status=True)
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Contacts.objects.filter(status=True)
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

class vwContactsTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeContact_pk=None):
        queryset = Contacts.objects.filter(
            type_contact__pk=typeContact_pk,status=True
        )

        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeContact_pk=None, pk=None):
        queryset = Contacts.bjects.filter(
            type_contact__pk=typeContact_pk,status=True
        )
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(contact)

class vwContactsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Contacts.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Contacts.bjects.filter(
            user__pk=typeContact_pk,status=True
        )
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)


'''
--------------- Documents ---------------------
'''
class DocumentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()

class DocumentsTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeDocument_pk=None):
        queryset = Documents.objects.filter(
            type_document__pk=typeDocument_pk,status=True
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeDocument_pk=None,pk=None):
        queryset = Documents.objects.filter(
            type_document__pk=typeDocument_pk,status=True
        )
        document = get_object_or_404(queryset, pk=pk)
        serializer = DocumentsSerializer(document)
        return Response(serializer.data)

class vwDocumentsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Documents.objects.filter(
            administrator__pk=user_pk,status=True
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
        queryset = Documents.objects.filter(
            administrator__pk=user_pk,status=True
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

class EventsTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeEvent_pk=None):
        queryset = Events.objects.filter(
            type_event__pk=typeEvent_pk,status=True
        )

        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeEvent_pk=None, pk=None):
        queryset = Events.bjects.filter(
            type_event__pk=typeEvent_pk,status=True
        )
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventsSerializer(contact)
        return Response(serializer.data)



'''
-------------- Favorites -------------------------
'''
class FavoritesViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


class vwFavoritesPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Favorites.objects.filter(
            publication__pk=publication_pk,status=True
        )

        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset = Favorites.bjects.filter(
            publication__pk=publication_pk,status=True
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

class vwNotificationsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Notifications.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = NotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            user__pk=user_pk,status=True
        )
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationsSerializer(notification)
        return Response(serializer.data)

class vwNotificationsPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Notifications.objects.filter(
            publication__pk=publication_pk,status=True
        )

        serializer = NotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            publication__pk=user_pk,status=True
        )
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationsSerializer(notification)
        return Response(serializer.data)


'''
----------------- Push Notifications  -----------------
'''
class PushNotificationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = PushNotificationsSerializer
    queryset = Push_Notifications.objects.all()

class vwPushNotificationsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Push_Notifications.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Push_Notifications.bjects.filter(
            user__pk=user_pk,status=True
        )
        push_notification = get_object_or_404(queryset, pk=pk)
        serializer = PushNotificationsSerializer(push_notification)
        return Response(serializer.data)

class vwPushNotificationsPubViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk,status=True
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk,status=True
        )
        push_notification = get_object_or_404(queryset, pk=pk)
        serializer = PushNotificationsSerializer(push_notification)
        return Response(serializer.data)

'''
--------------- Favorites Providers ---------------------
'''
class FavoritesProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesProvidersSerializer
    queryset = Favorites_Providers.objects.all()

class vwFavoritesProvidersViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Favorites_Providers.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = FavoritesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Favorites_Providers.objects.filter(
            user__pk=user_pk,status=True
        )
        favorite_provider = get_object_or_404(queryset, pk=pk)
        serializer = FavoritesProvidersSerializer(favorite_provider)
        return Response(serializer.data)

class vwProviderFavoritesProvidersViewSet(viewsets.ViewSet):
    def list(self, request,provider_pk=None):
        queryset = Favorites_Providers.objects.filter(
            provider__pk=provider_pk,status=True
        )

        serializer = FavoritesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,provider_pk=None, pk=None):
        queryset =Favorites_Providers.objects.filter(
            provider__pk=provider_pk,status=True
        )
        favorite_provider = get_object_or_404(queryset, pk=pk)
        serializer = FavoritesProvidersSerializer(favorite_provider)
        return Response(serializer.data)

'''
------------------- Photos ----------------------------
'''
class PhotosViewSet(viewsets.ModelViewSet):
 
    serializer_class = PhotosSerializer
    queryset = Photos.objects.all()

class vwPhotosPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Photos.objects.filter(
            publication__pk=publication_pk,status=True
        )

        serializer =PhotosSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset =Photos.objects.filter(
            publication__pk=publication_pk,status=True
        )
        photo = get_object_or_404(queryset, pk=pk)
        serializer = PhotosSerializer(photo)
        return Response(serializer.data)

'''
----------------- Types Reports --------------------
'''
class TypesReportsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesReportsSerializer
    queryset = Types_Reports.objects.all()

class vwAllTypesReportsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Reports.objects.filter(status=True)
        serializer =ReportsSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset =Reports.objects.filter(status=True)
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
    def list(self, request,user_pk=None):
        queryset = Reports.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Reports.objects.filter(
            user__pk=user_pk,status=True
        )
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)

class vwTypeReportsViewSet(viewsets.ViewSet):
    def list(self, request,typeReport_pk=None):
        queryset = Reports.objects.filter(
            type_report__pk=typeReport_pk,status=True
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeReport_pk=None, pk=None):
        queryset =Reports.objects.filter(
            type_report__pk=typeReport_pk,status=True
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
    def list(self, request,user_pk=None):
        queryset = User_Location.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = UserLocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =User_Location.objects.filter(
            user__pk=user_pk,status=True
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

class vwAllTypesCustomersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Customers.objects.filter(status=True)
        serializer = TypeCustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset =Types_Customers.objects.filter(status=True)
        type_customer = get_object_or_404(queryset, pk=pk)
        serializer = TypeCustomersSerializer(type_customer)
        return Response(serializer.data)

'''
--------------  Customers ----------------------
'''
class CustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all() 

class vwCustomerViewSet(viewsets.ViewSet):
    def list(self, request,contact_pk=None):
        queryset = Customers.objects.filter(
            contact__pk=contact_pk,status=True
        )

        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

class vwCustomersForTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeCustomer_pk=None):
        queryset =Customers.objects.filter(
            type_customer__pk=typeCustomer_pk,status=True
        )

        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeCustomer_pk=None, pk=None):
        queryset =Customers.objects.filter(
            type_customer__pk=typeCustomer_pk,status=True
        )
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomersSerializer(customer)
        return Response(serializer.data)    


'''
--------------- Favorites Customers -----------------------
'''
class FavoritesCustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesCustomersSerializer
    queryset = Favorites_Customers.objects.all() 

class vwFavoritesCustomersViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Favorites_Customers.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = FavoritesCustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Favorites_Customers.objects.filter(
            user__pk=user_pk,status=True
        )
        fav_custumer = get_object_or_404(queryset, pk=pk)
        serializer = FavoritesCustomersSerializer(fav_custumer)
        return Response(serializer.data)    

'''
--------------  Tasks ----------------------
'''
class TasksViewSet(viewsets.ModelViewSet):
 
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()   

class vwTasksViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Tasks.objects.filter(
            user__pk=user_pk,status=True
        )

        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Tasks.objects.filter(
            user__pk=user_pk,status=True
        )
        task = get_object_or_404(queryset, pk=pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)   

class vwTaskViewSet(viewsets.ViewSet):
    def list(self, request,contact_pk=None):
        queryset = Tasks.objects.filter(
            contact__pk=contact_pk,status=True
        )

        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)
  
class uploadFileViewSet(viewsets.ViewSet):
  parser_classes = (FileUploadParser,)
  def create(self, request,filename=None,type=None):
    file_obj = request.FILES['file']
    url=""
    return Response(file_obj.name,url, status=status.HTTP_201_CREATED, headers=headers)