var archiveApp = angular.module('blogArchive',['ngRoute','angularMoment']);

archiveApp.config(['$locationProvider','$interpolateProvider', function($locationProvider, $interpolateProvider){
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
  $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
  });
}]);


archiveApp.controller('ArchiveCtrl', function($scope,$route,$http,$location) {
      $scope.getAllPosts = function() {
          $http({
            method: 'GET',
            url: 'http://127.0.0.1:5000/archive/all_posts',
          })
          .then(function (data) {
            $scope.posts = JSON.parse(data.data.data);
            console.log($scope.posts[0]);
          }, function(errResponse) {
            return console.log(errResponse);
          });
      }; 
      $scope.getQueryParams = function() {
          $scope.query = $location.search().query || 'Narrow Results';
          console.log($location.search());
      };
      $scope.makeUtcReadable = function(utcStamp) {
          var d = new Date(0);
          d.setUTCSeconds(utcStamp);
          return d.toString().split(' ').slice(0,3).join(' ');
      };
  });
