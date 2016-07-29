
var firItem = parseFloat(prompt("What is your first item?"));
var secItem = parseFloat(prompt("What is your second item?"));
var coup = parseFloat(prompt("Your coupon?"));
var tax = parseFloat(prompt("What is the salestax?"));

checkout(firItem,secItem,coup,tax);

//checkout(50,35,0.25,0.095);
function checkout(item1, item2, coupon, salesTax){
  var subtotal = item1 + item2;
  var couponAmount = subtotal * coupon;
  var total = subtotal - couponAmount;
  var moreMoney = total * salesTax;
  var finalTotal = total + moreMoney ;
  finalTotal= finalTotal.toFixed(2);
  //return finalTotal;
  alert("Your total is " + finalTotal);
}

/*var myTotal= checkout(50,35,0.25,0.095);
alert("Total amount on bleh" + mytotal)*/
