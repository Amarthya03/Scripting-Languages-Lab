// The function HourMinute(num) must return the number of hours and minutes the parameter converts
// to. Separate the number of hours and minutes with a colon.
// E.g. Input : 126 Output : 2:6
// E.g. Input : 45 Output : 0:45
    
var x = 157;
var h = parseInt(x/60, 10);
var m = parseInt(x%60, 10);
var res = h + ":" + m;
console.log(res);