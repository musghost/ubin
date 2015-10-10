from rest_framework import serializers

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


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id','name','status')

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id','name', 'country','status')

class StatesFullSerializer(serializers.ModelSerializer):
    country=CountriesSerializer()
    class Meta:
        model = States
        fields = ('id','name', 'country','status')

class TownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Towns
        fields = ('id','name','state','status')

class TownsFullSerializer(serializers.ModelSerializer):
    state=StatesFullSerializer()
    class Meta:
        model = Towns
        fields = ('id','name','state','status')

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id','name','town','status')

class NeighborhoodFullSerializer(serializers.ModelSerializer):
    town=TownsFullSerializer()
    class Meta:
        model = Neighborhood
        fields = ('id','name','town','status')

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('id','name', 'status')

class TypesImmovablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Immovables
        fields = ('id','name', 'status')

class TypesPublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Publications
        fields = ('id','name', 'status')

class TypesAdvisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Advisors
        fields = ('id','name', 'status')

class TypesProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Providers
        fields = ('id','name', 'status')

class TypesContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Contacts
        fields = ('id','name', 'status')

class TypesEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Events
        fields = ('id','name', 'status')

class TypesDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Documents
        fields = ('id','name', 'status')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'email',
            'password',
            'name',
            'last_name',
            'mother_last_name',
            'birthday',
            'gender',
            'phone',
            'type_advisor',
            'immovable_name',
            'immovable_phone',
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

class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = (
        	'id',
        	'name',
        	'type_provider',
            'neighborhood',
        	'town',
        	'register_date',
        	'address',
        	'email',
        	'web_page',
        	'status'
        	)

class ClassificationProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification_Providers
        fields = ('id','score','user','provider','status')

class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = (
        	'id',
        	'canvas_number',
        	'user', 
        	'type_publications',
        	'type_immovable',
            'neighborhood',
        	'town',
        	'title',
        	'description',
        	'price_first',
        	'price_second',
        	'currency',
        	'bathrooms',
        	'old',
        	'ground_surface',
        	'construction_area',
        	'country',
        	'state',
        	'date',
        	'status'
        	)
class PublicationsFullSerializer(serializers.ModelSerializer):
    type_publications=TypesPublicationsSerializer()
    type_immovable=TypesImmovablesSerializer()
    neighborhood=NeighborhoodFullSerializer()
    currency=CurrenciesSerializer()
    user=UsersSerializer()
    class Meta:
        model = Publications
        fields = (
            'id',
            'canvas_number',
            'user', 
            'type_publications',
            'type_immovable',
            'neighborhood',
            'town',
            'title',
            'description',
            'price_first',
            'price_second',
            'currency',
            'bathrooms',
            'old',
            'ground_surface',
            'construction_area',
            'country',
            'state',
            'date',
            'status'
            )

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
        	'id',
        	'publication',
        	'user', 
        	'comment',
        	'date',
            'status'
        	)

class CommentsFullerializer(serializers.ModelSerializer):
    user=UsersSerializer()
    class Meta:
        model = Comments
        fields = (
            'id',
            'publication',
            'user', 
            'comment',
            'date',
            'status'
            )


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
        	'id',
        	'name',
        	'lastname', 
        	'phone',
        	'email',
        	'user',
        	'type_contact',
        	'note',
            'is_favorite'
            'status'
        	)

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = (
        	'id',
        	'name',
        	'administrator', 
        	'type_document',
        	'path',
            'status'
        	)

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
        	'id',
        	'name',
        	'description', 
        	'type_event',
            'date_event',
            'administrator',
            'status'
        	)

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id','publication','user', 'status')

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = (
        	'id',
        	'publication',
        	'user', 
        	'message',
        	'date',
        	'read',
        	'viewed',
        	'expired',
            'status'
        	)

class PushNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Push_Notifications
        fields = (
        	'id',
        	'publication',
        	'user', 
        	'device_token',
        	'device',
        	'status',
        	'date'
        	)

class FavoritesProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites_Providers
        fields = ('id','user','provider','status')

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = (
        	'id',
        	'name',
        	'path',
        	'publication',
            'status'
        	)
class TypesReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Reports
        fields = (
        	'id',
        	'name',
        	'status',
        	)

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = (
        	'id',
        	'user',
        	'type_report',
        	'message',
        	'date',
            'status'
        	)

class UserUbicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Ubication
        fields = (
        	'id',
        	'user',
        	'country',
        	'state',
        	'date',
            'status'
        	)

class TypeCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Customers
        fields = ('id','name','status')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = (
            'id',
            'name',
            'last_name',
            'mother_last_name',
            'phone',
            'email',
            'contact',
            'type_customer',
            'status'
            )

class FavoritesCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites_Customers
        fields = ('id','customer','user','status')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            'id',
            'description',
            'date',
            'hour',
            'contact',
            'user',
            'status'
            )

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = (
            'id',
            'text',
            'date',
            'status'
            )