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
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

 
class CountriesViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
 
class StatesViewSet(viewsets.ModelViewSet):
    #authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = StatesSerializer
    queryset = States.objects.all()

class TownsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TownsSerializer
    queryset = Towns.objects.all()

class CoinsViewSet(viewsets.ModelViewSet):
 
    serializer_class = CoinsSerializer
    queryset = Coins.objects.all()

class TypesImmovablesViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesImmovablesSerializer
    queryset = Types_Immovables.objects.all()

class TypesPublicationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesPublicationsSerializer
    queryset = Types_Publications.objects.all()

class TypesAdvisorsViewSet(viewsets.ModelViewSet):
 
    serializer_class = TypesAdvisorsSerializer
    queryset = Types_Advisors.objects.all()

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


class UsersViewSet(viewsets.ModelViewSet):
 
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class ProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ProvidersSerializer
    queryset = Providers.objects.all()

class ClassificationProvidersViewSet(viewsets.ModelViewSet):
 
    serializer_class = ClassificationProvidersSerializer
    queryset = Classification_Providers.objects.all()

class PublicationsViewSet(viewsets.ModelViewSet):
 
    serializer_class = PublicationsSerializer
    queryset = Publications.objects.all()

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