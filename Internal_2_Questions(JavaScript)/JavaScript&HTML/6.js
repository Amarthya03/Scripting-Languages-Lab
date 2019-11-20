console.log("Connected!");
var leli = [];
var max = 0;
var x = document.querySelector("input");
var button = document.querySelector("button");
var res = document.querySelector("#res");
button.addEventListener("click", function(){
    var str = x.value;
    var list = str.split(" ");
    for(var i =0; i<list.length; i++) {
        leli[i] = list[i].length;
    }
    for(var i=0; i<leli.length; i++) {
        if(leli[i]>max){
            max = leli[i];
        }
    }
    res.textContent = max;
    max = 0;
});