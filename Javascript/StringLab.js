var text = "ELEPHANTBEARMOUSECOW";
var first = text.indexOf("MOUSE");
var two = text.indexOf("E",first);

var firstHalf = text.substr(0,first);
var length = text.length;
var secHalf = text.substr(two+1,length);
var mouse = text.substring(first,two+1);
newMouse = mouse.toLowerCase();

var newText = firstHalf + newMouse + secHalf;
alert(newText);
