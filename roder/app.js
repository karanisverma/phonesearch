(function() {
        var app = angular.module('mobile-app', ['ngMaterial']);
        app.controller('phoneAppController', ['$http', function($http) {
                var phoneApp = this;
                $http.get('http://karanverma.me/js/mobiledata.json').success(function(data) {
                    phoneApp.mobile = data;
                    // console.log("PHONE DATA =>>>> ",phoneApp.mobile);
                });
                this.ranker = function(ram_rating, camera_rating, storage_rating, battery_rating) {
                    // console.log("worked!!");
                    // console.log("Printing it from"+phoneApp.mobile);
                    console.log(ram_rating + ", " + camera_rating + ", " + storage_rating + ", " + battery_rating);

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

                        var rank = (ram_r * (ram / 2)) + (camera_r * (camera / 8)) + (storage_r * (storage / 8)) + (battery_r * (battery / 2100));
                        phoneApp.mobile[i].rank = rank;
                        // console.log(rank);

                        // if (rank > phoneApp.minrank()) 
                        //     {
                        //         phoneApp.add_to_top_ten(index,phoneApp.mobile[i]);
                        //     }
                    }

                    phoneApp.result = phoneApp.rank_sort(phoneApp.mobile);
                    console.log("-------------------------------------");
                    console.log(phoneApp.result);
                    console.log("-------------------------------------");
                    // phoneApp.dummy();

                    // and show it to the user
                    // 1,2,3,4,5

                }

                this.dummy = function() {
                    console.log("dummy is working");
                }

                this.rank_sort = function(unsorted){
                    var sotrting_array = unsorted.slice(0);

                    sotrting_array.sort(function(a, b) {
                        return a.rank - b.rank;
                    });
                    array_len = sotrting_array.length
                    sorted_array = sotrting_array.slice(array_len-10,array_len);

                    for (i = 0; i < sorted_array.length; i++) {
                        console.log(sorted_array[i].rank);
                    }
                return sorted_array;
            }
            // this.minrank = function(){
            //     // find the min rank of given array and return index of the 
            //     // min rank object
            // }
            // this.add_to_top_ten = function(){
            //     // addes object into array and returns the new updated array
            //     // of top 10 objects
            // }


        }]); //closing controller
    app.config(function($mdThemingProvider) {
        $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
        $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
        $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
        $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
    });
})();
