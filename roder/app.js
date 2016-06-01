(function(){
var app = angular.module('mobile-app', ['ngMaterial']);
app.controller('phoneAppController', ['$http', function($http) {
    var phoneApp = this;
    var search = function(rating2,rating1,rating3,rating4){
        console.log(rating2+", "+rating1+", "+rating3+", "+rating4);
    }
    
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
