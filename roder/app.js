(function(){
var app = angular.module('mobile-app', ['ngMaterial']);
app.controller('phoneAppController', ['$http', function($http) {
    var phoneApp = this;
    phoneApp.mobile="ya y iaskh dkjldjove bhiukadsfjk"; // pdata stands for phone data.
    // var test = "yada-yada-yadayada-yada";
    $http.get('http://karanverma.me/js/mobiledata.json').success(function(data) {
        phoneApp.mobile = data;  
        // console.log("PHONE DATA =>>>> ",phoneApp.mobile);
    });
    
     //closing success data 
}]); //closing controller
app.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
  $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
  $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
  $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
});
})();
