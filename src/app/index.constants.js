/* global malarkey:false, toastr:false, moment:false */
(function() {
  'use strict';

  angular
    .module('ubin')
    .constant('malarkey', malarkey)
    .constant('toastr', toastr)
    .constant('moment', moment)
    .constant('HOST', 'http://192.168.59.103:8000/api/v1/api-token-auth/');

})();
