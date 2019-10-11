function HourMinute(num) {
    var h = parseInt(num/60);
    var m = parseInt(num%60);
    console.log(h+":"+m);
}
HourMinute(126)
