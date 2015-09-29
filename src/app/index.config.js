(function() {
  'use strict';

  angular
    .module('ubin')
    .config(config);

  /** @ngInject */
  function config($logProvider, $authProvider, toastr) {
    // Enable log
    $logProvider.debugEnabled(true);

    // Set options third-party lib
    toastr.options.timeOut = 3000;
    toastr.options.positionClass = 'toast-top-right';
    toastr.options.preventDuplicates = true;
    toastr.options.progressBar = true;

    //Set conf parameter of $authProvider
    $authProvider.loginUrl = 'http://192.168.59.103:8000/api/v1/api-token-auth/';
    $authProvider.tokenName = 'token';
    $authProvider.tokenPrefix = 'ubin';
  }

})();
