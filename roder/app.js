(function(){
var app = angular.module('mobile-app', ['ngMaterial']);
app.controller('phoneAppController', ['$http', function($http) {
    var phoneApp = this;
    $http.get('http://karanverma.me/js/mobiledata.json').success(function(data) {
        phoneApp.mobile = data;  
        // console.log("PHONE DATA =>>>> ",phoneApp.mobile);
    });
    this.ranker = function(rating1,rating2,rating3,rating4){
        // console.log("worked!!");
        // console.log("Printing it from"+phoneApp.mobile);
        console.log(rating2+", "+rating1+", "+rating3+", "+rating4);
        for (i = 0; i < phoneApp.mobile.length; i++) { 
            console.log(phoneApp.mobile[i].name);
}
        // TODO :
        // apply for-loop for each product in data 
        // and get the ranking out of it 
        // assign it to some value like mobile.rankers
        // and show it to the user
    }
    this.dummy = function(){
        console.log("dummy is working");
    }

    
     //closing success data 
}]); //closing controller
app.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
  $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
  $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
  $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
});
})();
