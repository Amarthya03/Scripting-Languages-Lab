console.log("Connected!");
var btn1 = document.querySelector("#btn1");
var btn2 = document.querySelector("#btn2");
var x = document.querySelector("input");
var res = document.querySelector("span");

btn1.addEventListener("click", function(){
    if(isNaN(x.value)){
        res.textContent = x.value + " is not a number";
    }
    var ans = x.value * 2;
    res.textContent = ans;
})
btn2.addEventListener("click", function(){
    if(isNaN(x.value)){
        res.textContent = x.value + " is not a number";
    }
    ans = x.value * x.value;
    res.textContent = ans;
})