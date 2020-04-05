

# Accessing an element in an array
array = [9,4,5,7,0]

print (array[3])
# output = 7

# print (array[9])---> This will print  "list index out of range" since the index at 9 is not available. 


# Insertion operation in an array
# One can add one or more element in an array at the end, beginning or any given index 
# Insertion takes two arguments, the index to insert the element and the element , i,e insert(i, element)
array = [9,4,5,7,0]

array.insert(0,3)  # the zero(0) is the first index and 3 is the element

print (array)  #  output --> [3, 9, 4, 5, 7, 0]

array.insert(4,8)   

print (array) # output --> [3, 9, 4, 5, 8, 7, 0]



# Deletion operation in an array
# Remove an exixting element in an array with the python inbult function remove()

array = [9,4,5,7,0]
array.remove(7) 

print(array) # removes the number 7 specified in the function and re-organizes the array



# Search operation in an array
# the search operation searches an element based on the index given or its value
# It uses in-built python function index()
array = [9,4,5,7,0] 

print (array.index(4)) # output ---> this returns 1 since index of 4 is 1
# print (array.index(3))  # output ---> this returns an ValueError since 3 is not in the array list 


# Update operation in an array 
# this operation updates an exixting element in the array by re-assigning a new value to an element by index.
array = [9,4,5,7,0] 
array[0] = 3

print (array)  # output --->[3, 4, 5, 7, 0] upadates value at index 0 to 3 and removes 9

array = [9,4,5,7,0] 
# array[5] = 3 This will return an error since the index at 5 is out of range...index goes upto 4
# print (array) - IndexError: list assignment index out of range