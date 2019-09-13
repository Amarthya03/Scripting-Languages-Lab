# Write a python program to read in a list of elements
# Create a new list that holds in all the elements minus the duplicates

def remove_duplicates(numbers):
    newlist = []
    for n in numbers:
        if n not in newlist:
            newlist.append(n)

    print(newlist)
    return(newlist)

remove_duplicates([1,2,3,4,5,5,5,6,3,2])
