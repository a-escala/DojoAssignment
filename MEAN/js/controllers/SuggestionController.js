app.controller('SuggestionController', ['$scope', '$routeParams', 'suggestions',
function($scope, $routeParams, suggestions){
  $scope.post = suggestions.posts[$routeParams.id];

$scope.addComment = function(){
  if(!$scope.comment || $scope.comment === ''){
    return;
  };
  $scope.post.comment.push({
    body: $scope.comment,
    upvotes: 0
  });
  $scope.comment = '';
  $scope.upVote = function(comment){
    comment.upVote += 1
  };
};
}]);
