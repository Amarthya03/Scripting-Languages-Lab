# Python has 5 data types: Number, String, List , Tuple, Dictionary
# Strings are immutable
# All the elements belonging to a list or tuple can be of different data type
# List elements and size can be changed
# Tuples are "read-only" lists. They are immutable. Once created, their size and elements cannot be changed
# We need tuples, because they are homogeneous, meaning they can store only one type of data
# Question: demo - 3

mydictionary = { "name": "Michael Corleone", "identity": "The Godfather", "age": 30 }
print(mydictionary)
key = mydictionary["name"]
value = mydictionary.get("name")
print("Key is", key)
print("Value is", value)
