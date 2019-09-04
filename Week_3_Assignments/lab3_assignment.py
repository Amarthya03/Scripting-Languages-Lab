class Student:                                              # Creating a class student with name, age and marks
    def __init__(self, name, age, marks):                   # Creating a constructor
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):                                      # Creating a display function 
        print("Name =", self.name, ",Age = ", self.age)
        print("Marks in 3 subjects: ")
        print(self.marks)

    def get_data(self):                                     # Asking user to enter the values
        print("Enter the details:")
        print("Name:")
        self.name = str(input())
        print("Age:")
        self.age = int(input())
        print("Marks in 3 subjects")
        for i in range(0,3):
            item = int(input())
            self.marks.append(item)

s = Student("",0,[])

s.get_data()
s.display()
