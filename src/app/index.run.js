(function() {
  'use strict';

  angular
    .module('ubin')
    .run(runBlock);

  /** @ngInject */
  function runBlock($log) {

    $log.debug('runBlock end');
  }

})();
