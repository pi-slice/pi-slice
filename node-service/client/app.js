var evens = [2,4,6,8];

var each = function(array, callback){
 for (var i = 0; i < array.length; i++){
   callback(array[i])
 }
};

result = each(evens, function(item){console.log(item + 1)});

var map = function(array, callback){
 var newArray = [];
 for (var i = 0; i < array.length; i++){
   newArray[i] = callback(array[i])
 }
 return newArray;
};

var result = map(evens, function(item){return(item * 4)});

console.log(result);
