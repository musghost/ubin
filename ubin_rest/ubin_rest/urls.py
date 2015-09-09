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
from apprest.viewsets import AdministratorsViewSet
from apprest.viewsets import UsersViewSet
from apprest.viewsets import ProvidersViewSet
from apprest.viewsets import ClassificationProvidersViewSet
from apprest.viewsets import PropertyProvidersViewSet
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

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'countries', CountriesViewSet)
router.register(r'states', StatesViewSet)
router.register(r'tows', TownsViewSet)
router.register(r'coins',CoinsViewSet)
router.register(r'typesImmovables',TypesImmovablesViewSet)
router.register(r'typesProperty',TypesPropertyViewSet)
router.register(r'typesAdvisors',TypesAdvisorsViewSet)
router.register(r'typesProviders',TypesProvidersViewSet)
router.register(r'typesContacts',TypesContactsViewSet)
router.register(r'typesEvents',TypesEventsViewSet)
router.register(r'typesDocuments',TypesDocumentsViewSet)
router.register(r'typesPhotos',TypesPhotosViewSet)
router.register(r'administrators',AdministratorsViewSet)
router.register(r'users',UsersViewSet)
router.register(r'providers',ProvidersViewSet)
router.register(r'classificationProviders',ClassificationProvidersViewSet)
router.register(r'propertyProviders',PropertyProvidersViewSet)
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
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
