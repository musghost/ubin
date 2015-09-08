from rest_framework import serializers

from .models import Countries
from .models import States
from .models import Towns
from .models import Coins
from .models import Types_Immovables
from .models import Types_Property
from .models import Types_Advisors
from .models import Types_Providers
from .models import Coins
from .models import Types_Immovables
from .models import Types_Property
from .models import Types_Advisors
from .models import Types_Providers
from .models import Types_Contacts
from .models import Types_Events
from .models import Types_Documents
from .models import Types_Photos
from .models import Administrators
from .models import Users
from .models import Providers
from .models import Classification_Providers
from .models import Property
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


from .serializers import CountriesSerializer
from .serializers import StatesSerializer
from .serializers import TownsSerializer
from .serializers import TypesImmovablesSerializer
from .serializers import TypesPropertySerializer
from .serializers import TypesAdvisorsSerializer
from .serializers import TypesProvidersSerializer
from .serializers import TypesContactsSerializer
from .serializers import TypesEventsSerializer
from .serializers import TypesDocumentsSerializer
from .serializers import TypesPhotosSerializer
from .serializers import AdministratorsSerializer
from .serializers import UsersSerializer
from .serializers import ProvidersSerializer
from .serializers import ClassificationProvidersSerializer
from .serializers import PropertySerializer
from .serializers import CommentsSerializer
from .serializers import ContactsSerializer
from .serializers import DocumnetsSerializer
from .serializers import EventsSerializer
from .serializers import FavoritesSerializer
from .serializers import NotificationsSerializer
from .serializers import NotificationsPushSerializer
from .serializers import FavoritesProvidersSerializer
from .serializers import PhotosSerializer
from .serializers import TypesReportsSerializer
from .serializers import ReportsSerializer
from .serializers import UserUbicationSerializer

from rest_framework import viewsets
 
class CountriesViewSet(viewsets.ModelViewSet):
 
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()
 
class AutorViewSet(viewsets.ModelViewSet):
 
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()
    
