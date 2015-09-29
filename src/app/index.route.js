(function() {
  'use strict';

  angular
    .module('ubin')
    .config(routeConfig);

  /** @ngInject */
  function routeConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'app/main/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .state('auth', {
        url: '/auth',
        templateUrl: 'app/auth/auth.html',
        controller: 'AuthController',
        controllerAs: 'auth'
      })
      .state('users-admin', {
        url: '/users/admin',
        templateUrl: 'app/admin-users/admin.html',
        controller: 'AdminController',
        controllerAs: 'admin'
      })
      .state('users-admin-new', {
        url: '/users/admin/new',
        templateUrl: 'app/admin-users/add.html',
        controller: 'AdminController',
        controllerAs: 'admin'
      })
      .state('users-clients', {
        url: '/clients',
        templateUrl: 'app/admin-users/clients.html',
        controller: 'AdminController',
        controllerAs: 'admin'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
