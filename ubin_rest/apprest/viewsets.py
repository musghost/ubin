from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Countries
from .models import States
from .models import Towns
from .models import Neighborhood
from .models import Currencies
from .models import Types_Immovables
from .models import Types_Publications
from .models import Types_Advisors
from .models import Types_Providers
from .models import Types_Immovables
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
from .models import User_Ubication
from .models import Types_Customers
from .models import Customers
from .models import Favorites_Customers
from .models import Tasks
from .models import Terms

from .serializers import CountriesSerializer
from .serializers import StatesSerializer
from .serializers import TownsSerializer
from .serializers import TownsFullSerializer
from .serializers import NeighborhoodFullSerializer
from .serializers import NeighborhoodSerializer
from .serializers import CurrenciesSerializer
from .serializers import TypesImmovablesSerializer
from .serializers import TypesPublicationsSerializer
from .serializers import TypesAdvisorsSerializer
from .serializers import TypesProvidersSerializer
from .serializers import TypesContactsSerializer
from .serializers import TypesEventsSerializer
from .serializers import TypesDocumentsSerializer
from .serializers import UsersSerializer
from .serializers import ProvidersSerializer
from .serializers import ClassificationProvidersSerializer
from .serializers import PublicationsSerializer
from .serializers import CommentsSerializer
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
from .serializers import UserUbicationSerializer
from .serializers import TypeCustomersSerializer
from .serializers import CustomersSerializer
from .serializers import FavoritesCustomersSerializer
from .serializers import TasksSerializer
from .serializers import TermsSerializer

'''
-----------  Countries --------------------------
'''
class CountriesViewSet(viewsets.ModelViewSet):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()

class vwCountriesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Countries.objects.all()
        serializer = CountriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        queryset = Countries.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CountriesSerializer(country)

        return Response(serializer.data)
'''
-----------  Sates --------------------------
''' 
class StatesViewSet(viewsets.ModelViewSet):

    serializer_class = StatesSerializer
    queryset = States.objects.all()

class vwStatesViewSet(viewsets.ViewSet):
    def list(self, request, country_pk=None):
        queryset = States.objects.filter(
            country__pk=country_pk
        )

        serializer = StatesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, country_pk=None, pk=None):
        queryset = States.objects.filter(
            country__pk=country_pk
        )
        state = get_object_or_404(queryset, pk=pk)
        serializer = StatesSerializer(state)

        return Response(serializer.data)

class vwStatesTownsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = States.objects.all()
        serializer = StatesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = States.objects.all()
        state = get_object_or_404(queryset, pk=pk)
        serializer = StatesSerializer(state)

        return Response(serializer.data)

'''
-----------  Towns --------------------------
'''
class TownsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TownsSerializer
    queryset = Towns.objects.all()

class vwTownsViewSet(viewsets.ViewSet):
    def list(self, request,country_pk=None,state_pk=None):
        queryset = Towns.objects.filter(
            state__pk=state_pk
        )

        serializer = TownsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,country_pk=None,state_pk=None, pk=None):
        queryset = Towns.objects.filter(
            state__pk=state_pk
        )
        town = get_object_or_404(queryset, pk=pk)
        serializer = TownsSerializer(town)
        return Response(serializer.data)

class TownsFullViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Towns.objects.all()

        serializer = TownsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Towns.objects.all()
        town = get_object_or_404(queryset, pk=pk)
        serializer = TownsFullSerializer(town)
        return Response(serializer.data)

class vwTownsStatesViewSet(viewsets.ViewSet):
    def list(self, request,state_pk=None):
        queryset = Towns.objects.filter(
            state__pk=state_pk
        )

        serializer = TownsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,state_pk=None, pk=None):
        queryset = Towns.objects.filter(
            state__pk=state_pk
        )
        town = get_object_or_404(queryset, pk=pk)
        serializer = TownsSerializer(town)

        return Response(serializer.data)

'''
----------------- Neighborhood --------------------
'''
class NeighborhoodViewSet(viewsets.ModelViewSet):
 
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()

class NeighborhoodFullViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Neighborhood.objects.all()

        serializer = NeighborhoodFullSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Neighborhood.objects.all()
        neighborhood = get_object_or_404(queryset, pk=pk)
        serializer = NeighborhoodFullSerializer(neighborhood)

        return Response(serializer.data)

'''
-----------  Currencies --------------------------
'''
class CurrenciesViewSet(viewsets.ModelViewSet):
 
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()

class vwCurrenciesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Currencies.objects.all()
        serializer = CurrenciesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Currencies.objects.all()
        currency = get_object_or_404(queryset, pk=pk)
        serializer = CurrenciesSerializer(currency)

        return Response(serializer.data)


'''
-----------  Types immovable --------------------------
'''

class TypesImmovablesViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesImmovablesSerializer
    queryset = Types_Immovables.objects.all()

class vwTypesImmovablesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Immovables.objects.all()
        serializer = TypesImmovablesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Immovables.objects.all()
        type_immovable = get_object_or_404(queryset, pk=pk)
        serializer = TypesImmovablesSerializer(type_immovable)

        return Response(serializer.data)


'''
-----------  Types Publications --------------------------
'''

class TypesPublicationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesPublicationsSerializer
    queryset = Types_Publications.objects.all()

class vwTypesPublicationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Publications.objects.all()
        serializer = TypesPublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Publications.objects.all()
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
        queryset = Types_Advisors.objects.all()
        serializer = TypesAdvisorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
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

class vwTypesProvidersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Providers.objects.all()
        serializer = TypesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Providers.objects.all()
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
        queryset = Types_Contacts.objects.all()
        serializer = TypesContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Contacts.objects.all()
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
        queryset = Types_Events.objects.all()
        serializer = TypesEventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
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

class vwTypesDocumentsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Documents.objects.all()
        serializer = TypesDocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Types_Documents.objects.all()
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
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class AdvisorUsersViewSet(viewsets.ViewSet):
    def list(self, request,typeAdvisor_pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk
        )

        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeAdvisor_pk=None,pk=None):
        queryset = Users.objects.filter(
            type_advisor__pk=typeAdvisor_pk
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
            type_provider__pk=typeProvider_pk
        )

        serializer = ProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeProvider_pk=None, pk=None):
        queryset = Providers.objects.filter(
            type_provider__pk=provider_pk
        )
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersSerializer(provider)

        return Response(serializer.data)

class vwProvidersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Providers.objects.all()
        serializer = ProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Providers.objects.all()
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProvidersSerializer(provider)

        return Response(serializer.data)



'''
---------------- Calssifications Providers ---------------------
'''
class ClassificationProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ClassificationProvidersSerializer
    queryset = Classification_Providers.objects.all()

class vwClassificationProvidersViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk
        )

        serializer = ClassificationProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            user__pk=user_pk
        )
        classificationPro = get_object_or_404(queryset, pk=pk)
        serializer = ClassificationProvidersSerializer(classificationPro)

        return Response(serializer.data)

class vwProviderClassificationProvidersViewSet(viewsets.ViewSet):
    def list(self, request,provider_pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk
        )

        serializer = ClassificationProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,provider_pk=None, pk=None):
        queryset = Classification_Providers.objects.filter(
            provider__pk=provider_pk
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

class vwPublicationsInTypeImmovableViewSet(viewsets.ViewSet):
    def list(self, request,typeImmovable_pk=None):
        queryset = Publications.objects.filter(
            type_immovable__pk=typeImmovable_pk
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeImmovable_pk=None,pk=None):
        queryset = Publications.objects.filter(
            type_immovable__pk=typeImmovable_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsInTypePublicationViewSet(viewsets.ViewSet):
    def list(self, request,typePublication_pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typePublication_pk=None,pk=None):
        queryset = Publications.objects.filter(
            type_publications__pk=typePublication_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsCurrenciesViewSet(viewsets.ViewSet):
    def list(self, request,currency_pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,currency_pk=None,pk=None):
        queryset = Publications.objects.filter(
            currency__pk=currency_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
        queryset = Publications.objects.filter(
            user__pk=user_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)

class vwAllPublicationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Publications.objects.all()

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Publications.objects.all()
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
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
            user__pk=user_pk
        )

        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
        queryset = Comments.objects.filter(
            user__pk=user_pk
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

class vwCommentsPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Comments.objects.filter(
            publication__pk=publication_pk
        )

        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,publication_pk=None,pk=None):
        queryset = Comments.objects.filter(
            publication__pk=user_pk
        )
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)



'''
----------------  Contacts ---------------------
'''
class ContactsViewSet(viewsets.ModelViewSet):
 
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class vwAllContactsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contacts.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Contacts.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

class vwContactsTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeContact_pk=None):
        queryset = Contacts.objects.filter(
            type_contact__pk=typeContact_pk
        )

        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeContact_pk=None, pk=None):
        queryset = Contacts.bjects.filter(
            type_contact__pk=typeContact_pk
        )
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(contact)

class vwContactsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Contacts.objects.filter(
            user__pk=user_pk
        )

        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Contacts.bjects.filter(
            user__pk=typeContact_pk
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
            type_document__pk=typeDocument_pk
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeDocument_pk=None,pk=None):
        queryset = Documents.objects.filter(
            type_document__pk=typeDocument_pk
        )
        document = get_object_or_404(queryset, pk=pk)
        serializer = DocumentsSerializer(document)
        return Response(serializer.data)

class vwDocumentsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Documents.objects.filter(
            administrator__pk=user_pk
        )

        serializer = DocumentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None,pk=None):
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

class EventsTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeEvent_pk=None):
        queryset = Events.objects.filter(
            type_event__pk=typeEvent_pk
        )

        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeEvent_pk=None, pk=None):
        queryset = Events.bjects.filter(
            type_event__pk=typeEvent_pk
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
            publication__pk=publication_pk
        )

        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
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

class vwNotificationsViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = Notifications.objects.filter(
            user__pk=user_pk
        )

        serializer = NotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            user__pk=user_pk
        )
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationsSerializer(notification)
        return Response(serializer.data)

class vwNotificationsPublicationsViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Notifications.objects.filter(
            publication__pk=publication_pk
        )

        serializer = NotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset = Notifications.bjects.filter(
            publication__pk=user_pk
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
            user__pk=user_pk
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset = Push_Notifications.bjects.filter(
            user__pk=user_pk
        )
        push_notification = get_object_or_404(queryset, pk=pk)
        serializer = PushNotificationsSerializer(push_notification)
        return Response(serializer.data)

class vwPushNotificationsPubViewSet(viewsets.ViewSet):
    def list(self, request,publication_pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk
        )

        serializer = PushNotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset = Push_Notifications.objects.filter(
            publication__pk=publication_pk
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
            user__pk=user_pk
        )

        serializer = FavoritesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Favorites_Providers.objects.filter(
            user__pk=user_pk
        )
        favorite_provider = get_object_or_404(queryset, pk=pk)
        serializer = FavoritesProvidersSerializer(favorite_provider)
        return Response(serializer.data)

class vwProviderFavoritesProvidersViewSet(viewsets.ViewSet):
    def list(self, request,provider_pk=None):
        queryset = Favorites_Providers.objects.filter(
            provider__pk=provider_pk
        )

        serializer = FavoritesProvidersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,provider_pk=None, pk=None):
        queryset =Favorites_Providers.objects.filter(
            provider__pk=provider_pk
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
            publication__pk=publication_pk
        )

        serializer =PhotosSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request,publication_pk=None, pk=None):
        queryset =Photos.objects.filter(
            publication__pk=publication_pk
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
        queryset = Reports.objects.all()
        serializer =ReportsSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset =Reports.objects.all()
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
            user__pk=user_pk
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Reports.objects.filter(
            user__pk=user_pk
        )
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)

class vwTypeReportsViewSet(viewsets.ViewSet):
    def list(self, request,typeReport_pk=None):
        queryset = Reports.objects.filter(
            type_report__pk=typeReport_pk
        )

        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeReport_pk=None, pk=None):
        queryset =Reports.objects.filter(
            type_report__pk=typeReport_pk
        )
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data)


'''
-------------- User Ubication ------------------------
'''
class UserUbicationViewSet(viewsets.ModelViewSet):
 
    serializer_class = UserUbicationSerializer
    queryset = User_Ubication.objects.all()

class vwUserUbicationViewSet(viewsets.ViewSet):
    def list(self, request,user_pk=None):
        queryset = User_Ubication.objects.filter(
            user__pk=user_pk
        )

        serializer = UserUbicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =User_Ubication.objects.filter(
            user__pk=user_pk
        )
        user_u = get_object_or_404(queryset, pk=pk)
        serializer = UserUbicationSerializer(user_u)
        return Response(serializer.data)

''''
----------------- Type Customers --------------------
'''
class TypeCustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypeCustomersSerializer
    queryset = Types_Customers.objects.all()

class vwAllTypesCustomersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Types_Customers.objects.all()
        serializer = TypeCustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset =Types_Customers.objects.all()
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
            contact__pk=contact_pk
        )

        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

class vwCustomersForTypeViewSet(viewsets.ViewSet):
    def list(self, request,typeCustomer_pk=None):
        queryset =Customers.objects.filter(
            type_customer__pk=typeCustomer_pk
        )

        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,typeCustomer_pk=None, pk=None):
        queryset =Customers.objects.filter(
            type_customer__pk=typeCustomer_pk
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
            user__pk=user_pk
        )

        serializer = FavoritesCustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Favorites_Customers.objects.filter(
            user__pk=user_pk
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
            user__pk=user_pk
        )

        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,user_pk=None, pk=None):
        queryset =Tasks.objects.filter(
            user__pk=user_pk
        )
        task = get_object_or_404(queryset, pk=pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)   

class vwTaskViewSet(viewsets.ViewSet):
    def list(self, request,contact_pk=None):
        queryset = Tasks.objects.filter(
            contact__pk=contact_pk
        )

        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)
  
class TermsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()   
 
