function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function fadeWhenClicked(){
  $("#pig").fadeToggle();
}

function slideWhenClicked(){
  $("#pig").slideToggle();

}
function bob(e) {
$('#pig').offset({
    left: e.pageX,
    top: e.pageY + 20
});
}
function flyWhenClicked(){
  $(document).mousemove(bob);
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#fadePig").click(fadeWhenClicked);
    $("#slidePig").click(slideWhenClicked);
    $("#flyingPig").click(flyWhenClicked);
}

$(document).ready(setup);
