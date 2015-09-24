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
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib import admin
admin.autodiscover()

from apprest.viewsets import CountriesViewSet
from apprest.viewsets import vwCountriesViewSet
from apprest.viewsets import StatesViewSet
from apprest.viewsets import vwStatesViewSet
from apprest.viewsets import vwStatesTownsViewSet
from apprest.viewsets import TownsViewSet
from apprest.viewsets import vwTownsViewSet
from apprest.viewsets import vwTownsStatesViewSet
from apprest.viewsets import CoinsViewSet
from apprest.viewsets import TypesImmovablesViewSet
from apprest.viewsets import vwTypesImmovablesViewSet
from apprest.viewsets import TypesPublicationsViewSet
from apprest.viewsets import vwTypesPublicationsViewSet
from apprest.viewsets import TypesAdvisorsViewSet
from apprest.viewsets import TypesProvidersViewSet
from apprest.viewsets import TypesContactsViewSet
from apprest.viewsets import TypesEventsViewSet
from apprest.viewsets import TypesDocumentsViewSet
from apprest.viewsets import TypesPhotosViewSet
from apprest.viewsets import UsersViewSet
from apprest.viewsets import ProvidersViewSet
from apprest.viewsets import ClassificationProvidersViewSet
from apprest.viewsets import PublicationsViewSet
from apprest.viewsets import vwPublicationsInTypeImmovableViewSet
from apprest.viewsets import vwPublicationsInTypePublicationViewSet
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
from apprest.viewsets import TermsViewSet

#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

#router = DefaultRouter()
router = routers.SimpleRouter()
'''
Countries
'''
#CRUD
router.register(r'country',CountriesViewSet)

#VIEW : /countries/pk/states/pk/towns/pk
router.register(r'countries',vwCountriesViewSet,base_name='countries')
vw_countries=routers.NestedSimpleRouter(router, r'countries',lookup='country')
vw_countries.register(r'states',vwStatesViewSet,base_name='states')
vw_towns=routers.NestedSimpleRouter(vw_countries,r'states',lookup='state')
vw_towns.register(r'towns',vwTownsViewSet,base_name='towns')

'''
States
'''
#CRUD
router.register(r'state',StatesViewSet)

#VIEW : /states/pk/towns/pk
router.register(r'states',vwStatesTownsViewSet,base_name='states')
vw_state_tows=routers.NestedSimpleRouter(router, r'states',lookup='state')
vw_state_tows.register(r'towns',vwTownsStatesViewSet,base_name="towns")

'''
Towns
'''
router.register(r'town', TownsViewSet)

'''
Coins
'''
router.register(r'coins',CoinsViewSet)

'''
Types Immovables
'''
#CRUD
router.register(r'typeImmovable',TypesImmovablesViewSet)

#VIEW : /typesImmovables/pk/publications/pk
router.register(r'typesImmovables',vwTypesImmovablesViewSet,base_name="typesImmovables")
vw_immovable_publications=routers.NestedSimpleRouter(router, r'typesImmovables',lookup='typeImmovable')
vw_immovable_publications.register(r'publications',vwPublicationsInTypeImmovableViewSet,base_name='publications')

'''
Types Publications
'''
#CRUD
router.register(r'typePublication',TypesPublicationsViewSet)
#VIEW : /typesPublications/pk/publications/pk
router.register(r'typesPublications',vwTypesPublicationsViewSet,base_name='typesPublications')
vw_type_publications=routers.NestedSimpleRouter(router, r'typesPublications',lookup='typePublication')
vw_type_publications.register(r'publications',vwPublicationsInTypePublicationViewSet,base_name='publications')

router.register(r'typesAdvisors',TypesAdvisorsViewSet)
router.register(r'typesProviders',TypesProvidersViewSet)
router.register(r'typesContacts',TypesContactsViewSet)
router.register(r'typesEvents',TypesEventsViewSet)
router.register(r'typesDocuments',TypesDocumentsViewSet)
router.register(r'typesPhotos',TypesPhotosViewSet)
router.register(r'terms',TermsViewSet)

router.register(r'users',UsersViewSet)

router.register(r'providers',ProvidersViewSet)

router.register(r'classificationProviders',ClassificationProvidersViewSet)

router.register(r'publications',PublicationsViewSet)

router.register(r'comments',CommentsViewSet)

router.register(r'contacts',ContactsViewSet)

router.register(r'documents',DocumentsViewSet)

router.register(r'events',EventsViewSet)

router.register(r'favorites',FavoritesViewSet)

router.register(r'notifications',NotificationsViewSet)

router.register(r'notificationsPush',NotificationsPushViewSet)

router.register(r'favoritesProviders',FavoritesProvidersViewSet)

router.register(r'photos',PhotosSerializerViewSet)


router.register(r'typesReports',TypesReportsViewSet)

router.register(r'reports',ReportsViewSet)

router.register(r'userLocation',UserUbicationViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^',include(vw_countries.urls)),
    url(r'^',include(vw_towns.urls)),
    url(r'^',include(vw_state_tows.urls)),
    url(r'^',include(vw_immovable_publications.urls)),
    url(r'^',include(vw_type_publications.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]   
