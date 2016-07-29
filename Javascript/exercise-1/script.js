//Event handler
function fadeImage(){
  $('img').fadeToggle();
}
function setup(){
  $('#android').click(fadeImage);
}
$(document).ready(setup);
