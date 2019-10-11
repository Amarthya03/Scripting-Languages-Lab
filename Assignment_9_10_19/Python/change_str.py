def ChangeStr(str):
    newstr = ''
    vow = ['a','e','i','o','u']
    nl = list(str)
    for i in range(0,len(nl)):
        nl[i] = chr(ord(nl[i])+1)
        if nl[i] in vow:
            nl[i] = nl[i].upper()
        newstr = newstr+nl[i]
    return(newstr)

str = str(input("Enter the string"))
res = ChangeStr(str)
print(res)
