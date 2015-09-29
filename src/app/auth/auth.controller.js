(function() {
  'use strict';

  angular
    .module('ubin')
    .controller('AuthController', AuthController);

  /** @ngInject */
  function AuthController($auth, $state, $http, HOST) {
    var vm = this;
    this.login = function () {
    	console.log('login');
    	$auth.login({
    		email: vm.email,
    		password: vm.password
    	})
    	.then(function(){
    		$state.go('users-admin');

    	})
    	.catch(function(response){
    		console.log(response);
    	});
    };
  }
})();
