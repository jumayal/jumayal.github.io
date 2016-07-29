var hitOnce = true;

function becomeSquare(){
  $('img').animate({
    width:"10px"
  })
}

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

  $('img').mouseover(
    function (e){
      $(this).css({"border-radius": "0px"});
    }
  );

  $('img').mouseleave(
    function (e){
      $(this).css({
        "border-radius": "200px"
      });
    }
  );
  $('.imagebox').click(
    function(event){
      if (hitOnce == true){

        $(this).animate({
          padding: "100%"
        });

        $(this).find('img').animate({
          width:"500px",
          height:"500px"
        });
        $(this).find('.textslide').slideDown();

        $(this).css({
          "background-color": "rgba(212, 204, 204, 0.50)",
          "z-index":"2",
          "position": "absolute",
          "top": "50%",
          "left": "50%",
          "margin-right": "-50%",
          "transform": "translate(-50%, -50%)",
          "-webkit-background-clip": "border",
          "position": "fixed"
        });

        hitOnce=false;

      }else{

        $(this).find('.textslide').slideUp();

        $(this).animate({
          padding: "0%"
        });

        $(this).find('img').animate({
          width: "300px",
          height: "300px",
        })

        $(this).css({
          "background-color":"transparent",
          "position": "relative",
          "top": "auto",
          "left": "auto",
          "margin-right": "0",
          "transform": "none",
          "-webkit-background-clip": "border-box"
        });
        hitOnce=true;
      }
    }
  );
}

$(document).ready(setup);
