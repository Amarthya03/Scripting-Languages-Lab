console.log("Connected!");
var x = document.querySelector("input");
var res = document.querySelector("span");
var btn = document.querySelector("button");
btn.addEventListener("click", function(){
    if(x.value%7==0){
        res.textContent = x.value + " is divisible by 7"
    }
    else if(x.value%3==0) {
        res.textContent = x.value + " is divisible by 3"
    }
    else if(isNaN(x.value)){
        res.textContent = x.value + " is not a number"
    }
    else {
        res.textContent = x.value + " is neither divisible by 3 or 7"
    }
})