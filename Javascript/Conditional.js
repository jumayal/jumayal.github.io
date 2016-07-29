var score = parseFloat(prompt("What is your Score?"));
rate(score);
function rate (s){
  if(s<150){
    alert("Im sorry but not sorry You Suck");
  }else if(s<250){
    alert("Not to shabby, but not good");
  }else if (s<350){
    alert("Thats good");
  }else{
    alert("Thats great man");
  }
}
