def OddRange(num1,num2):
    l = num1
    h = num2
    list= []
    for i in range(l,h):
        if i % 2 != 0:
            list.append(i)
    return list

x = OddRange(0,13)
print(x)
