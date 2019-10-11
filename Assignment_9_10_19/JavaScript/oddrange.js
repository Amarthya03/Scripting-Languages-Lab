function OddRange(num1, num2) {
    var l = num1;
    var h = num2;
    for(i=l;i<h;i++) {
        if(i%2 !==0){
            console.log(i);
        }
    }
}
OddRange(3,13);
