class temperature():
    def __init__(self,val):
        self.val = val

    def f_2_c(self):
        ans = (self.val-32)*5/9
        print(ans)
        return(ans)

    def c_2_f(self):
        ans = ((self.val)*9/5)+32
        print(ans)
        return(ans)

flag = 1
his = []

while flag is 1:

    t = float(input("Enter a value:\n"))

    obj = temperature(t)

    print("1. Celsius to Fahrenheit\t"
          "2. Fahrenheit to Celsius\t"
          "3. Exit\t"
          "4. Display")

    ch = int(input("Enter a choice:\n"))

    if ch is 1:
        item = obj.c_2_f()
        it = ("Celsius:",t,"Fahrenheit:",item)
        his.append(it)
    elif ch is 2:
        item = obj.f_2_c()
        it = ("Fahrenheit:",t,"Celsius:",item)
        his.append(it)
    elif ch is 3:
        flag = 0
    elif ch is 4:
        print(his)
