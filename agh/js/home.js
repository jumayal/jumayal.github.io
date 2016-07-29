function setup(){

  $(".allheader").mouseenter(
    function(){
      $(".slide").slideDown();
    }
  );

  $(".allheader").mouseleave(
    function() {
      $(".slide").slideUp();
    }
  );

  $(".link").mouseenter(
    function(){
      $(this).css({
        "border-style":"inset"
      });
    }
  );

  $(".link").mouseleave(
    function(){
      $(this).css({
        "border-style":"outset"
      });
    }
  );
}
$(document).ready(setup);
