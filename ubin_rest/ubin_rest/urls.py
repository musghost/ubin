from django.conf.urls import include, url
from django.contrib.auth import login, authenticate, logout
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib import admin
admin.autodiscover()

from apprest.viewsets import *


from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()

router.register(r'country', CountryViewSet)
router.register(r'state', StateViewSet)
router.register(r'town', TownViewSet)
router.register(r'neighborhood', NeighborhoodViewSet)
router.register(r'neighborhoodFilter', NeighborhoodFilterViewSet)
router.register(r'townFilter', TownFilterViewSet)
router.register(r'stateFilter', StateFilterViewSet)

'''
Currencies
'''
# CRUD
router.register(r'currency', CurrenciesViewSet)
# VIEW
router.register(r'currencies', vwCurrenciesViewSet, base_name='currencies')
vw_currencies_publications = routers.NestedSimpleRouter(
    router, r'currencies', lookup='currency')
vw_currencies_publications.register(
    r'publications', vwPublicationsCurrenciesViewSet, base_name="publications")


'''
Types Property
'''
# CRUD
router.register(r'typeProperty', TypesPropertyViewSet)

# VIEW : /typesImmovables/pk/publications/pk
router.register(r'typesProperty', vwTypesPropertyViewSet,
                base_name="typesProperty")
vw_property_publications = routers.NestedSimpleRouter(
    router, r'typesProperty', lookup='typeProperty')
vw_property_publications.register(
    r'publications', vwPublicationsInTypeImmovableViewSet, base_name='publications')

'''
Types Publications
'''
# CRUD
router.register(r'typePublication', TypesPublicationsViewSet)
# VIEW : /typesPublications/pk/publications/pk
router.register(r'typesPublications', vwTypesPublicationsViewSet,
                base_name='typesPublications')
vw_type_publications = routers.NestedSimpleRouter(
    router, r'typesPublications', lookup='typePublication')
vw_type_publications.register(
    r'publications', vwPublicationsInTypePublicationViewSet, base_name='publications')

'''
Type Advisor
'''
# CRUD
router.register(r'typeAdvisor', TypesAdvisorsViewSet)
# VIEW : typesAdvisors/pk/user/pk
router.register(r'typesAdvisors', vwTypesAdvisorsViewSet,
                base_name='typesAdvisors')
vw_advisors_users = routers.NestedSimpleRouter(
    router, r'typesAdvisors', lookup='typeAdvisor')
vw_advisors_users.register(r'users', AdvisorUsersViewSet, base_name='users')

'''
Types Providers
'''
# CRUD
router.register(r'typeProvider', TypesProvidersViewSet)
# VIEW : typeProviders/pk/providers/pk
router.register(r'typesProviders', vwTypesProvidersViewSet,
                base_name='typesProviders')
vw_providers_type = routers.NestedSimpleRouter(
    router, r'typesProviders', lookup='typeProvider')
vw_providers_type.register(
    r'providers', vwProvidersTypeViewSet, base_name='providers')


'''
Types Events
'''
# CRUD
router.register(r'typeEvent', TypesEventsViewSet)
# VIEW typesEvents/pk/events/pk
router.register(r'typesEvents', vwTypesEventsViewSet, base_name='typesEvents')
vw_events_type = routers.NestedSimpleRouter(
    router, r'typesEvents', lookup='typeEvent')

'''
Types documents
'''
# CRUD
router.register(r'typeDocument', TypesDocumentsViewSet)
# VIEW typesDocuments/pk/documents/pk
router.register(r'typesDocuments', vwTypesDocumentsViewSet,
                base_name='typesDocuments')
vw_type_documents = routers.NestedSimpleRouter(
    router, r'typesDocuments', lookup='typeDocument')
vw_type_documents.register(
    r'documents', DocumentsTypeViewSet, base_name='documents')


'''
users
'''
# CRUD
router.register(r'user', UsersViewSet, base_name='user')
router.register(r'users', vwUsersViewSet, base_name='users')
# Filter
router.register(r'usersFilter', UsersFilterViewSet)
# VIEW : /users/pk/clasificationProviders/pk
vw_classifications_providers = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_classifications_providers.register(
    r'clasificationProviders', vwClassificationProvidersViewSet, base_name='clasificationProviders')
# VIEW : /users/pk/publications/pk
vw_publications_users = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_publications_users.register(
    r'publications', vwPublicationsViewSet, base_name='publications')
# VIEW : /users/pk/comments/pk
vw_comments_users = routers.NestedSimpleRouter(router, r'users', lookup='user')
vw_comments_users.register(
    r'comments', vwCommentsViewSet, base_name='comments')
# VIEW : /users/pk/documents/pk
vw_documents_users = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_documents_users.register(
    r'documents', vwDocumentsViewSet, base_name='documents')
# VIEW : /users/pk/notifications/pk
vw_notifications_users = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_notifications_users.register(
    r'notifications', vwNotificationsViewSet, base_name='notifications')
# VIEW : /users/pk/pushNotifications/pk
vw_push_notifications_users = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_push_notifications_users.register(
    r'pushNotifications', vwPushNotificationsViewSet, base_name='pushNotifications')
# VIEW : /users/pk/reports/pk
vw_reports_users = routers.NestedSimpleRouter(router, r'users', lookup='user')
vw_reports_users.register(r'reports', vwReportsViewSet, base_name='reports')
# VIEW : /users/pk/userLocation/pk
vw_user_location_users = routers.NestedSimpleRouter(
    router, r'users', lookup='user')
vw_user_location_users.register(
    r'userLocation', vwUserLocationViewSet, base_name='userLocation')
# VIEW : /users/pk/tasks/pk
vw_tasks_users = routers.NestedSimpleRouter(router, r'users', lookup='user')
vw_tasks_users.register(r'tasks', vwTasksViewSet, base_name='tasks')

'''
Providers
'''
# CRUD
router.register(r'provider', ProvidersViewSet)
# FILTER
router.register(r'providersFilter', ProvidersDefaultFilterViewSet)
# VIEW : /providers/pk/clasificationProviders/pk
router.register(r'providers', vwProvidersViewSet, base_name='providers')
vw_classification_providers = routers.NestedSimpleRouter(
    router, r'providers', lookup='provider')
vw_classification_providers.register(
    r'clasificationProviders', vwProviderClassificationProvidersViewSet, base_name='clasificationProviders')

'''
Classification Providers 
'''
router.register(r'classificationProvider', ClassificationProvidersViewSet)

'''
Publications
'''
# CRUD
router.register(r'publication', PublicationsViewSet, base_name="publication")
# Filter
router.register(r'publicationsFilter', PublicationsDefaultFilterViewSet)
# VIEW : publications/pk/comments/pk
router.register(r'publications', vwAllPublicationsViewSet,
                base_name='publications')
vw_comments_publications = routers.NestedSimpleRouter(
    router, r'publications', lookup='publication')
vw_comments_publications.register(
    r'comments', vwCommentsPublicationsViewSet, base_name='comments')
# VIEW : publications/pk/favoritesPublications/pk
vw_favorites_publications = routers.NestedSimpleRouter(
    router, r'publications', lookup='publication')
vw_favorites_publications.register(
    r'favorites', vwFavoritesPublicationsViewSet, base_name='favorites')
# VIEW : publications/pk/notifications/pk
vw_notifications_publications = routers.NestedSimpleRouter(
    router, r'publications', lookup='publication')
vw_notifications_publications.register(
    r'notifications', vwNotificationsPublicationsViewSet, base_name='notifications')
# VIEW : publications/pk/pushNotifications/pk
vw_push_notifications_publications = routers.NestedSimpleRouter(
    router, r'publications', lookup='publication')
vw_push_notifications_publications.register(
    r'pushNotifications', vwPushNotificationsPubViewSet, base_name='pushNotifications')
# VIEW : publications/pk/photos/pk
vw_photos_publications = routers.NestedSimpleRouter(
    router, r'publications', lookup='publication')
vw_photos_publications.register(
    r'photos', vwPhotosPublicationsViewSet, base_name='photos')

'''
Comments
'''
router.register(r'comment', CommentsViewSet)
router.register(r'commentsFilter', CommentsFilterViewSet)


'''
Documents
'''
router.register(r'document', DocumentsViewSet, base_name='document')
# Filter
router.register(r'documentsFilter', DocumentsFilterViewSet)

'''
Events
'''
router.register(r'event', EventsViewSet)
router.register(r'eventsFilter', EventsFilterViewSet)

'''
Favorites
'''
router.register(r'favorite', FavoritesViewSet)
router.register(r'favoritesFilter', FavoritesFilterViewSet)
router.register(r'unfavorite', UnfavoriteViewSet, base_name="unfavorite")

'''
Notifications
'''
router.register(r'notification', NotificationsViewSet)
router.register(r'notificationsFilter', NotificationsFilterViewSet,
                base_name='notificationsFilter')

'''
Push Notifications
'''
router.register(r'pushNotification', PushNotificationsViewSet)


'''
Photos
'''
# CRUD
router.register(r'photo', PhotosViewSet)
# Filter
router.register('photosFilter', PhotosDefaultFilterViewSet)


'''
Types Customers
'''
# CRUD
router.register(r'typeCustomer', TypeCustomersViewSet)
# VIEW : typesCustomers/pk/customers/pk
router.register(r'typesCustomers', vwAllTypesCustomersViewSet,
                base_name='typesCustomers')
vw_types_customers = routers.NestedSimpleRouter(
    router, r'typesCustomers', lookup='typeCustomer')
vw_types_customers.register(
    r'customers', vwCustomersForTypeViewSet, base_name='customers')

'''
Types Reports
'''
# CRUD
router.register(r'typeReport', TypesReportsViewSet)
# VIEW : /typesReports/pk/reports/pk
router.register(r'typesReports', vwAllTypesReportsViewSet,
                base_name='typesReports')
vw_types_reports = routers.NestedSimpleRouter(
    router, r'typesReports', lookup='typeReport')
vw_types_reports.register(
    r'reports', vwTypeReportsViewSet, base_name='reports')

'''
Reports
'''
router.register(r'report', ReportsViewSet)

'''
Users Location
'''
router.register(r'userLocation', UserLocationViewSet)

'''
Customers
'''
router.register(r'customer', CustomersViewSet)
router.register(r'customersFilter', CustomersFilterViewSet)


'''
Tasks
'''
router.register(r'task', TasksViewSet)
router.register(r'tasksFilter', TasksFilterViewSet)


'''
Devices user register
'''
# CRUD
router.register(r'device', DevicesUserRegisterViewSet)
# Filter
router.register(r'deviceFilter', DevicesUserRegisterDefaultFilterViewSet)

'''
Register
'''
# CRUD
router.register(r'register', RegisterViewSet, base_name="register")

'''
Create token
'''
# CRUD
router.register(r'api-token-auth', GetTokenViewSet, base_name="api-token-auth")

'''
Recover password
'''
# CRUD
router.register(r'recoverPassword', RecoverPasswordViewSet,
                base_name="recoverPassword")

'''
logout
'''
# CRUD
router.register(r'logout', LogoutViewSet, base_name="logout")

'''
Type publications to past due portfolio
'''
# CRUD
router.register(r'typePublicationsPastDue', TypesPublicationsPastDueViewSet)

'''
Legal status
'''
# CRUD
router.register(r'legalStatus', LegalStatusViewSet)

urlpatterns = [
    url(r'^api/v1/admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^api/v1/api-token-refresh/',
        'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/v1/', include(vw_property_publications.urls)),
    url(r'^api/v1/', include(vw_type_publications.urls)),
    url(r'^api/v1/', include(vw_currencies_publications.urls)),
    url(r'^api/v1/', include(vw_advisors_users.urls)),
    url(r'^api/v1/', include(vw_providers_type.urls)),
    url(r'^api/v1/', include(vw_events_type.urls)),
    url(r'^api/v1/', include(vw_type_documents.urls)),
    url(r'^api/v1/', include(vw_classifications_providers.urls)),
    url(r'^api/v1/', include(vw_publications_users.urls)),
    url(r'^api/v1/', include(vw_comments_users.urls)),
    url(r'^api/v1/', include(vw_documents_users.urls)),
    url(r'^api/v1/', include(vw_notifications_users.urls)),
    url(r'^api/v1/', include(vw_push_notifications_users.urls)),
    url(r'^api/v1/', include(vw_reports_users.urls)),
    url(r'^api/v1/', include(vw_user_location_users.urls)),
    url(r'^api/v1/', include(vw_tasks_users.urls)),
    url(r'^api/v1/', include(vw_classification_providers.urls)),
    url(r'^api/v1/', include(vw_comments_publications.urls)),
    url(r'^api/v1/', include(vw_favorites_publications.urls)),
    url(r'^api/v1/', include(vw_notifications_publications.urls)),
    url(r'^api/v1/', include(vw_push_notifications_publications.urls)),
    url(r'^api/v1/', include(vw_photos_publications.urls)),
    url(r'^api/v1/', include(vw_types_customers.urls)),
    url(r'^api/v1/', include(vw_types_reports.urls)),
    url(r'^api/v1/api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),

]
