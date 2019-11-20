// The functio n AgeConvert(num) needs to calculate the age of a person, given the birth date.
// E.g. Input : 28-02-1992 Output : 27
function calculate_age(dob) { 
    var diff_ms = Date.now() - dob.getTime();
    var age_dt = new Date(diff_ms); 
  
    return Math.abs(age_dt.getUTCFullYear() - 1970);
}

console.log(calculate_age(new Date(1999, 5, 3)));
