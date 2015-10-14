from rest_framework import serializers

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



class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('id','name', 'status')

class TypesPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Property
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

class ProvidersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Providers
        fields = (
        	'id',
        	'name',
        	'type_provider',
        	'register_date',
        	'address',
        	'email',
        	'web_page',
            'state',
            'neighborhood',
            'town',
        	'status'
        	)

class ProvidersFullSerializer(serializers.ModelSerializer):
    type_provider=TypesProvidersSerializer()
    class Meta:
        model = Providers
        fields = (
            'id',
            'name',
            'type_provider',
            'register_date',
            'address',
            'email',
            'web_page',
            'state',
            'neighborhood',
            'town',
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
        	'type_property',
        	'title',
        	'description',
        	'price_first',
        	'price_second',
        	'currency',
        	'bathrooms',
        	'antiquity',
        	'area',
        	'construction_area',
        	'country',
        	'state',
            'town',
            'neighborhood',
        	'date',
        	'status'
        	)
class PublicationsFullSerializer(serializers.ModelSerializer):
    type_publications=TypesPublicationsSerializer()
    type_property=TypesPropertySerializer()
    currency=CurrenciesSerializer()
    user=UsersSerializer()
    class Meta:
        model = Publications
        fields = (
            'id',
            'canvas_number',
            'user', 
            'type_publications',
            'type_property',
            'title',
            'description',
            'price_first',
            'price_second',
            'currency',
            'bathrooms',
            'antiquity',
            'area',
            'construction_area',
            'country',
            'state',
            'town',
            'neighborhood',
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
    publication=PublicationsSerializer()
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
            'mothers_maiden_name',
        	'phone',
        	'email',
        	'user',
        	'type_contact',
        	'note',
            'is_favorite',
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

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Location
        fields = (
        	'id',
        	'user',
        	'country',
        	'state',
            'town',
            'neighborhood',
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
            'mothers_maiden_name',
            'phone',
            'email',
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