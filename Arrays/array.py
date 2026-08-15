from array import array

# Create an integer array
arr = array('i', [10, 20, 30, 40, 50])

print("Original array:", arr)

# append() - adds an element at the end
arr.append(60)
print("After append:", arr)

# insert() - adds an element at a specific position
arr.insert(2, 25)
print("After insert:", arr)

# remove() - removes a specified element
arr.remove(40)
print("After remove:", arr)

# pop() - removes and returns the last element
x = arr.pop()
print("Popped element:", x)
print("After pop:", arr)

# index() - finds the position of an element
print("Index of 30:", arr.index(30))

# reverse() - reverses the array
arr.reverse()
print("After reverse:", arr)

# count() - counts occurrences of an element
print("Count of 20:", arr.count(20))

# len() - finds the number of elements
print("Length:", len(arr))