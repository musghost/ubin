"""ubin_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth import login, authenticate, logout
from rest_framework_nested import routers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib import admin
admin.autodiscover()

from apprest.viewsets import CountriesViewSet
from apprest.viewsets import StatesViewSet
from apprest.viewsets import TownsViewSet
from apprest.viewsets import CoinsViewSet
from apprest.viewsets import TypesImmovablesViewSet
from apprest.viewsets import TypesPropertyViewSet
from apprest.viewsets import TypesAdvisorsViewSet
from apprest.viewsets import TypesProvidersViewSet
from apprest.viewsets import TypesContactsViewSet
from apprest.viewsets import TypesEventsViewSet
from apprest.viewsets import TypesDocumentsViewSet
from apprest.viewsets import TypesPhotosViewSet
from apprest.viewsets import UsersViewSet
from apprest.viewsets import ProvidersViewSet
from apprest.viewsets import ClassificationProvidersViewSet
from apprest.viewsets import PropertyViewSet
from apprest.viewsets import CommentsViewSet
from apprest.viewsets import ContactsViewSet
from apprest.viewsets import DocumentsViewSet
from apprest.viewsets import EventsViewSet
from apprest.viewsets import FavoritesViewSet
from apprest.viewsets import NotificationsViewSet
from apprest.viewsets import NotificationsPushViewSet
from apprest.viewsets import FavoritesProvidersViewSet
from apprest.viewsets import PhotosSerializerViewSet
from apprest.viewsets import TypesReportsViewSet
from apprest.viewsets import ReportsViewSet
from apprest.viewsets import UserUbicationViewSet
from apprest.viewsets import TypeCustomersViewSet
from apprest.viewsets import CustomersViewSet
from apprest.viewsets import FavoritesCustomersViewSet
from apprest.viewsets import TasksViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'countries', CountriesViewSet)

router.register(r'states', StatesViewSet, base_name='states')
states_router = routers.NestedSimpleRouter(router, r'states', lookup='state')
states_router.register(r'country', CountriesViewSet, base_name='country')

router.register(r'towns', TownsViewSet, base_name='towns')

towns_router = routers.NestedSimpleRouter(router, r'towns', lookup='town')
towns_router.register(r'state', StatesViewSet, base_name='state')

towns_countries_router = routers.NestedSimpleRouter(towns_router, r'state', lookup='state')
towns_countries_router.register(r'country',CountriesViewSet, base_name='country')

router.register(r'coins',CoinsViewSet)
router.register(r'typesImmovables',TypesImmovablesViewSet)
router.register(r'typesProperty',TypesPropertyViewSet)
router.register(r'typesAdvisors',TypesAdvisorsViewSet)
router.register(r'typesProviders',TypesProvidersViewSet)
router.register(r'typesContacts',TypesContactsViewSet)
router.register(r'typesEvents',TypesEventsViewSet)
router.register(r'typesDocuments',TypesDocumentsViewSet)
router.register(r'typesPhotos',TypesPhotosViewSet)

router.register(r'users',UsersViewSet,base_name='users')
user_type_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_type_router.register(r'typeAdvisor', TypesAdvisorsViewSet, base_name='typeAdvisor')

router.register(r'providers',ProvidersViewSet,base_name='providers')
provider_type_router = routers.NestedSimpleRouter(router, r'providers', lookup='provider')
provider_type_router.register(r'typeProvider',TypesProvidersViewSet, base_name='typeProvider')
provider_town_router = routers.NestedSimpleRouter(router, r'providers', lookup='provider')
provider_town_router.register(r'town',TownsViewSet, base_name='town')

router.register(r'classificationProviders',ClassificationProvidersViewSet,base_name='classificationProviders')
classification_providers=routers.NestedSimpleRouter(router, r'classificationProviders', lookup='classificationProviders')
classification_providers.register(r'user',UsersViewSet, base_name='user')
classification_provider=routers.NestedSimpleRouter(router, r'classificationProviders', lookup='classificationProviders')
classification_provider.register(r'provider',ProvidersViewSet,base_name='provider')

router.register(r'property',PropertyViewSet,base_name='property')
property_user=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_user.register(r'user',UsersViewSet,base_name='user')
property_type_property=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_type_property.register(r'typeProperty',TypesPropertyViewSet,base_name='typeProperty')
property_type_immovable=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_type_immovable.register(r'typeImmovable',TypesImmovablesViewSet,base_name='typeImmovable')
property_town=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_town.register(r'town',TownsViewSet,base_name='town')
property_coin=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_coin.register(r'coin',CoinsViewSet,base_name='coin')
property_country=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_country.register(r'country',CountriesViewSet,base_name='country')
property_type_advisor=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_type_advisor.register(r'typeAdvisor',TypesAdvisorsViewSet,base_name='TypeAdvisor')
property_state=routers.NestedSimpleRouter(router, r'property', lookup='property')
property_state.register(r'state',StatesViewSet,base_name='state')

router.register(r'comments',CommentsViewSet,base_name='comments')
commets_property=routers.NestedSimpleRouter(router,r'comments',lookup='comment')
commets_property.register(r'property',PropertyViewSet,base_name='property')
commets_user=routers.NestedSimpleRouter(router,r'comments',lookup='comment')
commets_user.register(r'user',UsersViewSet,base_name='user')
commets_provider=routers.NestedSimpleRouter(router, r'comments', lookup='comment')
commets_provider.register(r'provider',ProvidersViewSet,base_name='provider')

router.register(r'contacts',ContactsViewSet,base_name="contact")
contacts_user=routers.NestedSimpleRouter(router,r'contacts',lookup='contact')
contacts_user.register(r'user',UsersViewSet,base_name='user')
type_contact=routers.NestedSimpleRouter(router,r'contacts',lookup='contact')
type_contact.register(r'typeContact',TypesContactsViewSet,base_name='typeContact')

router.register(r'documents',DocumentsViewSet,base_name='documents')
documents_user=routers.NestedSimpleRouter(router,r'documents',lookup='document')
documents_user.register(r'user',UsersViewSet,base_name='user')
type_document=routers.NestedSimpleRouter(router,r'documents',lookup='document')
type_document.register(r'typeDocument',DocumentsViewSet,base_name="typeDocument")

router.register(r'events',EventsViewSet,base_name="events")
event_user=routers.NestedSimpleRouter(router,r'events',lookup='event')
event_user.register(r'user',UsersViewSet,base_name='user')
type_event=routers.NestedSimpleRouter(router,r'events',lookup='event')
type_event.register(r'typeEvent',TypesEventsViewSet,base_name='typeEvent')
event_state=routers.NestedSimpleRouter(router,r'events',lookup='event')
event_state.register(r'state',StatesViewSet,base_name='state')
event_town=routers.NestedSimpleRouter(router,r'events',lookup='event')
event_town.register(r'town',TownsViewSet,base_name='town')

router.register(r'favorites',FavoritesViewSet,base_name='favorites')
favorite_property=routers.NestedSimpleRouter(router,r'favorites',lookup='favorite')
favorite_property.register(r'property',PropertyViewSet,base_name='property')
favorite_user=routers.NestedSimpleRouter(router,r'favorites',lookup='favorite')
favorite_user.register(r'user',UsersViewSet,base_name='user')

router.register(r'notifications',NotificationsViewSet,base_name='notifications')
notifications_property=routers.NestedSimpleRouter(router,r'notifications',lookup='notification')
notifications_property.register(r'property',PropertyViewSet,base_name='property')
notifications_user=routers.NestedSimpleRouter(router,r'notifications',lookup='notification')
notifications_user.register(r'user',UsersViewSet,base_name='user')

router.register(r'notificationsPush',NotificationsPushViewSet,base_name='notificationsPush')
notificationsPush_property=routers.NestedSimpleRouter(router,r'notificationsPush',lookup='notificationPush')
notificationsPush_property.register(r'property',PropertyViewSet,base_name='property')
notificationsPush_user=routers.NestedSimpleRouter(router,r'notificationsPush',lookup='notificationPush')
notificationsPush_user.register(r'user',UsersViewSet,base_name='user')

router.register(r'favoritesProviders',FavoritesProvidersViewSet,base_name='favoritesProviders')
favorite_provider_user=routers.NestedSimpleRouter(router,r'favoritesProviders',lookup='favoriteProvider')
favorite_provider_user.register(r'user',UsersViewSet,base_name='user')
favorite_provider=routers.NestedSimpleRouter(router,r'favoritesProviders',lookup='favoriteProvider')
favorite_provider.register(r'provider',ProvidersViewSet,base_name='provider')

router.register(r'photos',PhotosSerializerViewSet,base_name='photos')
photos_property=routers.NestedSimpleRouter(router,r'photos',lookup='photo')
photos_property.register(r'property',PropertyViewSet,base_name='property')
photos_provider=routers.NestedSimpleRouter(router,r'photos',lookup='photo')
photos_provider.register(r'provider',ProvidersViewSet,base_name='provider')
type_photo=routers.NestedSimpleRouter(router,r'photos',lookup='photo')
type_photo.register(r'typePhoto',TypesPhotosViewSet,base_name='typePhoto')

router.register(r'typesReports',TypesReportsViewSet)

router.register(r'reports',ReportsViewSet,base_name='reports')
reports_user=routers.NestedSimpleRouter(router,r'reports',lookup='report')
reports_user.register(r'user',UsersViewSet,base_name='user')
type_report=routers.NestedSimpleRouter(router,r'reports',lookup='report')
type_report.register(r'typeReport',UsersViewSet,base_name='typeReport')

router.register(r'userLocation',UserUbicationViewSet,base_name='userLocation')
location_user=routers.NestedSimpleRouter(router,r'userLocation',lookup='userLocation')
location_user.register(r'user',UsersViewSet,base_name='user')
location_country=routers.NestedSimpleRouter(router,r'userLocation',lookup='userLocation')
location_country.register(r'country',CountriesViewSet,base_name='country')
location_state=routers.NestedSimpleRouter(router,r'userLocation',lookup='userLocation')
location_state.register(r'state',StatesViewSet,base_name='state')

urlpatterns = [
    url(r'^api/v1/admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/v1/api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^', include(states_router.urls)),
    url(r'^', include(towns_router.urls)),
    url(r'^', include(towns_countries_router.urls)),
    url(r'^', include(user_type_router.urls)),
    url(r'^', include(provider_type_router.urls)), 
    url(r'^', include(provider_town_router.urls)),
    url(r'^', include(classification_providers.urls)),
    url(r'^', include(classification_provider.urls)), 
    url(r'^', include(property_user.urls)),  
    url(r'^', include(property_type_property.urls)),
    url(r'^', include(property_type_immovable.urls)),
    url(r'^', include(property_town.urls)),
    url(r'^', include(property_coin.urls)),
    url(r'^', include(property_country.urls)),
    url(r'^', include(property_type_advisor.urls)),
    url(r'^', include(property_state.urls)),
    url(r'^', include(commets_property.urls)),
    url(r'^', include(commets_user.urls)),
    url(r'^', include(commets_provider.urls)),
    url(r'^', include(contacts_user.urls)),
    url(r'^', include(type_contact.urls)),
    url(r'^', include(type_document.urls)),
    url(r'^', include(event_user.urls)),
    url(r'^', include(type_event.urls)),
    url(r'^', include(event_state.urls)),
    url(r'^', include(event_town.urls)),
    url(r'^', include(favorite_property.urls)),
    url(r'^', include(favorite_user.urls)),
    url(r'^', include(notifications_property.urls)),
    url(r'^', include(notifications_user.urls)),
    url(r'^', include(notificationsPush_property.urls)),
    url(r'^', include(notificationsPush_user.urls)),
    url(r'^', include(favorite_provider_user.urls)),
    url(r'^', include(favorite_provider.urls)),
    url(r'^', include(photos_property.urls)),
    url(r'^', include(photos_provider.urls)),
    url(r'^', include(type_photo.urls)),
    url(r'^', include(reports_user.urls)),
    url(r'^', include(type_report.urls)),
    url(r'^', include(location_user.urls)),
    url(r'^', include(location_country.urls)),
    url(r'^', include(location_state.urls)),
]   
