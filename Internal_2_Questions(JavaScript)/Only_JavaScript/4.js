// The function OddRange(num1, num2) takes two integers and needs to return an array of the odd
// numbers between the given integers.
var a = 1;
var b = 20;
var li = [];
var j = 0;
for(var i=a; i<=b; i++) {
    if(i%2!=0){
        li[j] = i;
        j++;
    }
}
console.log(li);