// The function ChangeString ( str ) needs to modify the string passed using the following rules:
// ● Replace every letter in the string with the letter that follows it in alphabetical order (ie. Z becomes a ,
// l becomes m ).
// ● Take every vowel in this new string (a, e, i, o, u) and Capitalize it.
// ● Return this modified string.
// E.g: Input : "hello*3" Output : Ifmmp*3

var str = "hello*3";
var v = ["a", "e", "i", "o", "u"];
var ns = "";
for(var i = 0; i< str.length; i++){
    if(str.charAt(i)>="a"&&str.charAt(i)<="z"){
        if(str.charAt(i)==="z"){
            ns = ns + "a";
        }
        else {
            var item = String.fromCharCode(str.charCodeAt(i)+1);
            ns = ns + item;
        }
    }
    else {
        ns = ns + str.charAt(i);
    }
}
for(i=0;i<ns.length; i++){
    for(var j =0; j<v.length; j++){
        if(ns.charAt(i)===v[j]){
            ns = ns.slice(0,i) + (ns.slice(i,i+1)).toUpperCase() + ns.slice(i+1);
        }
    }
}
console.log(ns);
