(function() {
var app = angular.module('phoneApp', []);
app.controller('phoneAppController', ['$http', function($http) {
    var pdata = this; // pdata stands for phone data.
    var test = "yada-yada-yada-yada-yada";
    $http.get('http://karanverma.me/js/phonedata.json').success(function(data) {
        pdata = data;
          
        console.log("PHONE DATA =>>>> ", pdata);
    });
	
     //closing success data 
}]); //closing controller

app.controller('testController',function(){
    var google = "kumbha karan";
	var wiki = "bhukkad";
});
})();