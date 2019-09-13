# Write a python program to read a list of numbers
# Use one line comprehension to create a new list of even numbers
# Create another reversed list

s = [i**2 for i in range(10)]
m = [i for i in s if i % 2 == 0]
m.reverse()

print(s)
print(m)