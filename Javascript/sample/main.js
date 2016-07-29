function addListItem(text){
  var list = document.querySelector('ul');
  var item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}

function addListItemJQuery(text){
  /*var list = $('ul');
  var item = document.createElement('li');
  item.innerText = text;
  list.append(item);
  */
  $('ul').append($('<li>').text(text));
}

//addListItem("Hey look at that! Your learning!");
addListItemJQuery("I'm here and here!!");
