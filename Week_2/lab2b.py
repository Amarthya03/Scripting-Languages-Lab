students = {'1MS17IS017':'Amarthya', '1MS17IS018':'Amit', '1MS17IS024':'Anirudh', '1MS17IS036':'Bhushan'}
list = ["value1","value2","value3","value4"]
list2 = []
j = 0
for i in students:
    print("Key is",i,"Value is", students[i])
    list[j] = students[i]
    j=j+1
print(list)
print(students.keys())
print(students.values())
print(students.items())

# Dictionaries are similar to hash-tables
