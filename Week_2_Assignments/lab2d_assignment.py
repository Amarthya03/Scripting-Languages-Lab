list = ["Robb","Jon","Sansa","Arya","Bran","Rickon"]    # Creating a list
n = len(list)                                           # Find the length of the list
print("Starks alive",list[1:5])                         # Slice operator
print(list)
print(n)

list[1] = "Cranberry"                                   #Replacing the secong element of the list
print(list)

list3 = ["Thomas","Arthur","Finn","John","Ada"]
list3.append(list)
print(list3)                                            #Creating a new list as an element of existing list

list2 = ["Jamie","Cersei","Tyrion"]
for i in list:
    list2.append(i)                                     #Concatenation of lists
print(list2)

for i in range(0,len(list2),3):
    print(list2[i])

list_new = [1,2,3,4,5,6]

lista = list_new[:int(len(list_new)/2)]
listb = list_new[int(len(list_new)/2):]
print(lista)
print(listb)
