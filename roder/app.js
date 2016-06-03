(function(){
var app = angular.module('mobile-app', ['ngMaterial']);
app.controller('phoneAppController', ['$http', function($http) {
    var phoneApp = this;
    $http.get('http://karanverma.me/js/mobiledata.json').success(function(data) {
        phoneApp.mobile = data;  
        // console.log("PHONE DATA =>>>> ",phoneApp.mobile);
    });
    this.ranker = function(ram_rating,camera_rating,storage_rating,battery_rating){
        // console.log("worked!!");
        // console.log("Printing it from"+phoneApp.mobile);
        console.log(ram_rating+", "+camera_rating+", "+storage_rating+", "+battery_rating);
       
        for (i = 0; i < phoneApp.mobile.length; i++) { 
            // console.log(phoneApp.mobile[i].name);
            var ram_r = parseInt(ram_rating);
            var camera_r = parseInt(camera_rating);
            var battery_r = parseInt(battery_rating);
            var storage_r = parseInt(storage_rating);

            var ram = parseInt(phoneApp.mobile[i].ram);
            var camera = parseInt(phoneApp.mobile[i].camera);
            var battery = parseInt(phoneApp.mobile[i].battery);
            var storage = parseInt(phoneApp.mobile[i].storage);

            var rank = (ram_r*(ram/2))+(camera_r*(camera/8))+(storage_r*(storage/8))+(battery_r*(battery/2100));
            phoneApp.mobile[i].rank = rank;
            console.log(rank)
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
