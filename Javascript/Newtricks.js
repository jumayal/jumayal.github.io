/*function clickHandler(){
  console.log("ClickHandler");
}

$("#myButton").click(clickHandler);
*/
$("#myButton").click(function(){
  var text = $('#textBox').val();
  //var item = document.createElement('li');
  //item.innerText = text;
  var myList = $('#myList');
  //myList.append(item)
  var spaceless
  if(text !== ""){
  myList.append("<li>" + text + "</li>");
  }
  $('#textBox').val("");
})

//Disable/Enable the button when the usertypes
$('#textBox').keypress(function(e){
  if($("textBox") !== ""){
  $()
  }
})
