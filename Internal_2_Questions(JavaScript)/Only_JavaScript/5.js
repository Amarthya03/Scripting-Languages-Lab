// The function LetterSurround(str) needs to find out if the string passed is an acceptable sequence by
// either returning true or false . The string parameter will be composed of + and = symbols with several
// characters between them. For the string to be true each letter must be surrounded by + symbol. Test
// Cases: The string will not be empty and will have at least one letter.
// E.g: Input : "+d+=3=+s+" Output : true
// E.g. Input : "f++d+" Output : false

function betterSurround(str)
{
    if((str.charAt(0) != '=' && str.charAt(0) != '+') || (str.charAt(str.length-1) != '=' && str.charAt(str.length-1) != '+'))
        return false
    else
    {
        for(var i =1;i<str.length-1;i++)
        {
            if(str.charAt(i)>='a' && str.charAt(i)<='z')
            {
                if(!(((str.charAt(i-1) == '+' || str.charAt(i-1) == '=') && (str.charAt(i+1) == '+' || str.charAt(i+1) == '='))))
                    return false
            }    
            else if(str.charAt(i-1)>='a' && str.charAt(i-1)<='z' && str.charAt(i+1)>='a' && str.charAt(i+1)<='z')
                return false

        }
    }
    return true
}

var newwrd = betterSurround("+f+=+d+")

if(newwrd)
    console.log("Yes")
else
    console.log("No")