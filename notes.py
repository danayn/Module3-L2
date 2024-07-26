'''
This is a note for Module 3 of Python Intermediate. 
This is a Multi-line String comment. 

LESSON 1: Python Tuples

# There are four collection data types in the Python programming language: List, Tuple, Set, and Dictionary.

https://www.w3schools.com/python/python_tuples.asp 

# Index
https://www.w3schools.com/python/ref_tuple_index.asp

# Unpack Tuples
https://www.w3schools.com/python/python_tuples_unpack.asp

# Join Tuples (+) -- concatenate
https://www.w3schools.com/python/python_tuples_join.asp


'''
# Tuples ( () ) are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List ( [] ), Set ( {} ), and Dictionary ( { : , :, } )
# , all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Tuple items are ordered, unchangeable, and allow duplicate values. First item is indexed -- [0]

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# length 
print(len(thistuple))

# Tuple can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = tuple(("apple", "banana", "cherry"))
print(tuple1)
print()
# Access Tuple items
print(thistuple[1])

# Negative Indexing -- Negative indexing means start from the end. 
#      -1 refers to the last item, -2 refers to the second last item etc. 
print(thistuple[-1])
print(thistuple[0:2])

#Single element tuple -- Python -- use comma --> (element,)



