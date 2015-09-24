from rest_framework import serializers

from .models import Countries
from .models import States
from .models import Towns
from .models import Coins
from .models import Types_Immovables
from .models import Types_Publications
from .models import Types_Advisors
from .models import Types_Providers
from .models import Coins
from .models import Types_Immovables
from .models import Types_Advisors
from .models import Types_Providers
from .models import Types_Contacts
from .models import Types_Events
from .models import Types_Documents
from .models import Types_Photos
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
from .models import Notifications_Push
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
from .serializers import CoinsSerializer
from .serializers import TypesImmovablesSerializer
from .serializers import TypesPublicationsSerializer
from .serializers import TypesAdvisorsSerializer
from .serializers import TypesProvidersSerializer
from .serializers import TypesContactsSerializer
from .serializers import TypesEventsSerializer
from .serializers import TypesDocumentsSerializer
from .serializers import TypesPhotosSerializer
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
from .serializers import NotificationsPushSerializer
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

from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication
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
-----------  Coins --------------------------
'''
class CoinsViewSet(viewsets.ModelViewSet):
 
    serializer_class = CoinsSerializer
    queryset = Coins.objects.all()

class vwCoinsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Coins.objects.all()
        serializer = CoinsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        queryset = Coins.objects.all()
        state = get_object_or_404(queryset, pk=pk)
        serializer = CoinsSerializer(state)

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
----------- Type Advisor --------------------------
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

class TypesProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesProvidersSerializer
    queryset = Types_Providers.objects.all()


class TypesContactsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesContactsSerializer
    queryset = Types_Contacts.objects.all()

class TypesEventsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesEventsSerializer
    queryset = Types_Events.objects.all()

class TypesDocumentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesDocumentsSerializer
    queryset = Types_Documents.objects.all()

class TypesPhotosViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesPhotosSerializer
    queryset = Types_Photos.objects.all()

'''
----------------  Users -------------------------
'''
class UsersViewSet(viewsets.ModelViewSet):
 
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

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


class ProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ProvidersSerializer
    queryset = Providers.objects.all()

class ClassificationProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ClassificationProvidersSerializer
    queryset = Classification_Providers.objects.all()

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

class vwPublicationsCoinsViewSet(viewsets.ViewSet):
    def list(self, request,coin_pk=None):
        queryset = Publications.objects.filter(
            coin__pk=coin_pk
        )

        serializer = PublicationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,coin_pk=None,pk=None):
        queryset = Publications.objects.filter(
            coin__pk=coin_pk
        )
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationsSerializer(publication)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

class ContactsViewSet(viewsets.ModelViewSet):
 
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class DocumentsViewSet(viewsets.ModelViewSet):
 
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()

class EventsViewSet(viewsets.ModelViewSet):
 
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class FavoritesViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()

class NotificationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = NotificationsSerializer
    queryset = Notifications.objects.all()

class NotificationsPushViewSet(viewsets.ModelViewSet):
 
    serializer_class = NotificationsPushSerializer
    queryset = Notifications_Push.objects.all()

class FavoritesProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesProvidersSerializer
    queryset = Favorites_Providers.objects.all()

class PhotosSerializerViewSet(viewsets.ModelViewSet):
 
    serializer_class = PhotosSerializer
    queryset = Photos.objects.all()

class TypesReportsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesReportsSerializer
    queryset = Types_Reports.objects.all()

class ReportsViewSet(viewsets.ModelViewSet):
 
    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()

class UserUbicationViewSet(viewsets.ModelViewSet):
 
    serializer_class = UserUbicationSerializer
    queryset = User_Ubication.objects.all()

class TypeCustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypeCustomersSerializer
    queryset = Types_Customers.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all() 

class FavoritesCustomersViewSet(viewsets.ModelViewSet):
 
    serializer_class = FavoritesCustomersSerializer
    queryset = Favorites_Customers.objects.all()     

class TasksViewSet(viewsets.ModelViewSet):
 
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()   

class TermsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()   