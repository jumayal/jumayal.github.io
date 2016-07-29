/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    //document.getElementById("myDropdown").classList.toggle("show");
    $("#myDropdown").show();
}

// Close the dropdown menu if the user clicks outside of it
window.onmouseover = function(event) {
  if (!event.target.matches('.dropbtn') && !event.target.matches('a')) {
    /*var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }*/
  $("#myDropdown").hide();
}
}
