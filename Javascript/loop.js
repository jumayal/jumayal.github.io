var animals = ["lion","tiger","bear","dog","koala","panda","ostrich","pig","racoon","monkey", "rat"];
var count = 0;
for(var i = 0;i < animals.length;i++){
  var word = animals[i];
  /*if(word.includes("a")){
    count= count+1;
  }*/
  for(var j = 0; j<word.length;i++){
    if(word.charAt(j) == "a"){
      count = count+1;
    }
  }
}
alert(count);
