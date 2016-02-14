from rest_framework import serializers

from .models import *
from rest_framework_jwt.settings import api_settings
from calendar import timegm
from datetime import datetime




class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('id','name','symbol','code','value','status')

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

class TypesEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Events
        fields = ('id','name', 'status')

class TypesDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Documents
        fields = ('id','name', 'status')

class RegisterSerializer(serializers.ModelSerializer):
    token=serializers.SerializerMethodField()
    type_advisor=TypesAdvisorsSerializer(required=False)
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
            'is_staff',
            'is_superuser',
            'register_date',
            'is_active',
            'token'
            )
    def get_token(self,obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = Users.objects.get(pk=obj.id,is_active=True)

        payload = jwt_payload_handler(user)

        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        token = jwt_encode_handler(payload)

        return token

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


class UsersFullSerializer(serializers.ModelSerializer):
    type_advisor=TypesAdvisorsSerializer()
    number_of_publications=serializers.SerializerMethodField()
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
            'number_of_publications',
            'is_active'
            )
    def get_number_of_publications(self,obj):
        number_of_publications=Publications.objects.filter(id=obj.id,status=True).count()
        return number_of_publications

class UsersDetailSerializer(serializers.ModelSerializer):
    type_advisor=TypesAdvisorsSerializer()
    number_of_publications=serializers.SerializerMethodField()
    class Meta:
        model = Users
        fields = (
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
            'register_date',
            'number_of_publications',
            'is_active'
            )
    def get_number_of_publications(self,obj):
        number_of_publications=Publications.objects.filter(id=obj.id,status=True).count()
        return number_of_publications


class ProvidersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Providers
        fields = (
        	'id',
        	'name',
            'references',
        	'type_provider',
        	'register_date',
            'phone',
        	'address',
        	'email',
        	'web_page',
            'state',
            'neighborhood',
            'town',
        	'status',
                'is_favorite',
                'administrator'
        	)

class ProvidersFullSerializer(serializers.ModelSerializer):
    hasVote=serializers.SerializerMethodField()
    totalScore=serializers.SerializerMethodField()
    average=serializers.SerializerMethodField()
    type_provider=TypesProvidersSerializer()
    class Meta:
        model = Providers
        fields = (
            'id',
            'name',
            'references',
            'type_provider',
            'register_date',
            'phone',
            'address',
            'email',
            'web_page',
            'state',
            'neighborhood',
            'town',
            'status',
            'is_favorite',
            'administrator',
            'hasVote',
            'totalScore',
            'average'
            )

    def get_hasVote(self,obj):
        if obj.score.all():
            return True
        else:
            return False
    def get_totalScore(self,obj):
        if obj.score.all():
            sum_votes=0
            for it in obj.score.all():
                print "escore"
                print it
                sum_votes+=it.score
            return sum_votes
        else:
            return 0
    def get_average(self,obj):
        try:
            from django.db.models import Avg
            average=Classification_Providers.objects.filter(
                        provider__pk=obj.id,
                        status=True
                ).aggregate(
                        average=Avg('score')
                )
            return average
        except:
            return 0





class ClassificationProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification_Providers
        fields = ('id','score','user','provider','status')

class ClassificationProvidersFullSerializer(serializers.ModelSerializer):
    provider=ProvidersFullSerializer()
    user=UsersDetailSerializer()
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
        	'currency',
        	'bathrooms',
        	'antiquity',
        	'area',
        	'construction_area',
        	'country',
        	'state',
            'town',
            'neighborhood',
            'is_mortgage',
            'code',
        	'date',
        	'status'
        	)

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = (
            'id',
            'hash_name',
            'original_name',
            'path',
            'publication',
            'status'
            )

class PublicationsFullSerializer(serializers.ModelSerializer):
    isfavorite=serializers.SerializerMethodField()
    votes=serializers.SerializerMethodField()
    type_publications=TypesPublicationsSerializer()
    type_property=TypesPropertySerializer()
    currency=CurrenciesSerializer()
    user=UsersDetailSerializer()
    photos=PhotosSerializer(many=True,read_only=True)
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
            'status',
            'is_mortgage',
            'code',
            'isfavorite',
            'votes',
            'photos'
            )
    def get_isfavorite(self,obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            favorite=Favorites.objects.filter(
                publication__id=obj.id,
                user__id=user.id
            )
            if favorite :
                return True
        return False

    def get_votes(self,obj):
        if obj.favorite.all():
            return obj.favorite.all().count()
        else:
            return 0
            
class CommentsFullerializer(serializers.ModelSerializer):
    user=UsersDetailSerializer()
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

class PublicationsNotificationSerializer(serializers.ModelSerializer):
    type_publications=TypesPublicationsSerializer()
    type_property=TypesPropertySerializer()
    currency=CurrenciesSerializer()
    user=UsersDetailSerializer()
    comments = CommentsFullerializer(many=True,read_only=True)
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
            'status',
            'is_mortgage',
            'code',
            'comments'
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


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = (
        	'id',
        	'original_name',
                'hash_name',
        	'administrator', 
        	'type_document',
        	'path',
                'country',
                'state',
                'town',
                'status'
        	)

class DocumentsFullSerializer(serializers.ModelSerializer):
    administrator=UsersDetailSerializer()
    type_document=TypesDocumentsSerializer()
    class Meta:
        model = Documents
        fields = (
            'id',
            'original_name',
            'hash_name',
            'administrator', 
            'type_document',
            'path',
            'country',
            'state',
            'town',
            'status'
            )

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
        	'id',
        	'name',
                'address',
        	'description', 
        	'type_event',
                'date_event',
                'hour',
                'administrator',
                'status'
        	)

class EventsFullSerializer(serializers.ModelSerializer):
    administrator=UsersDetailSerializer()
    type_event=TypesEventsSerializer()
    class Meta:
        model = Events
        fields = (
            'id',
            'name',
            'address',
            'description', 
            'type_event',
            'date_event',
            'hour',
            'administrator',
            'status'
            )

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id','publication','user', 'status')

class FavoritesFullSerializer(serializers.ModelSerializer):
    publication=PublicationsFullSerializer()
    user=UsersDetailSerializer()
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

class NotificationsFullSerializer(serializers.ModelSerializer):
    publication=PublicationsNotificationSerializer()
    user=UsersDetailSerializer()
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

class PhotosFullSerializer(serializers.ModelSerializer):
    publication=PublicationsFullSerializer()
    class Meta:
        model = Photos
        fields = (
            'id',
            'hash_name',
            'original_name',
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
            'user',
            'note',
            'type_customer',
            'is_favorite',
            'status'
            )

class CustomersFullSerializer(serializers.ModelSerializer):
    type_customer=TypeCustomersSerializer()
    user=UsersDetailSerializer()
    class Meta:
        model = Customers
        fields = (
            'id',
            'name',
            'last_name',
            'mothers_maiden_name',
            'phone',
            'email',
            'user',
            'note',
            'type_customer',
            'is_favorite',
            'status'
            )



class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            'id',
            'description',
            'date',
            'hour',
            'customer',
            'user',
            'status'
            )

class TasksFullSerializer(serializers.ModelSerializer):
    customer=CustomersFullSerializer()
    user=UsersDetailSerializer()
    class Meta:
        model = Tasks
        fields = (
            'id',
            'description',
            'date',
            'hour',
            'customer',
            'user',
            'status'
            )

class DevicesUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices_User_Register
        fields = (
                'id',
                'device_user',
                'device_os',
                'device_token',
                'device_register_date',
                'device_status'
            )

class DevicesUserRegisterFullSerializer(serializers.ModelSerializer):
    device_user=UsersDetailSerializer()
    class Meta:
        model = Devices_User_Register
        fields = (
                'id',
                'device_user',
                'device_os',
                'device_token',
                'device_register_date',
                'device_status'
            )
