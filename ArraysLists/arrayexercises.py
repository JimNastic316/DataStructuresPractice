def traversArray(array:list)->None:
    print('traversed arrays look like this')
    for item in array:
        print(item)
    print('*' * 40)

sep = ('*' * 40)
my_array = ['element0', 'element1', 'element2', 'element3', 'element4', 'element5']

# to print elements and type of element
print(my_array[0], type(my_array[0]))
print(my_array[1])

# to traverse an array

for i in my_array:
    print(i)


# appended vs inserted an element into an array

fruit = ['apple', 'banana', 'grape', 'lemon']
print(fruit)
# for f in fruit:
#     print(f)


fruit.append('appended cherry')
fruit.insert(2, 'inserted blueberry')
traversArray(fruit)



# pop removes element at specific position
# remove removes the first item with the specified value

names = ['Alex', 'Barry', 'Alex', 'Charlie', 'Dave']
traversArray(names)

names.pop(4)
print(names)

names.remove('Alex')
traversArray(names)

# searching for the first occurance of an element in an array
colors = ['red', 'blue', 'red', 'green', 'red', 'orange']
position = colors.index('green')
print(position)

print(sep)

# sorting an array
noombahs = [99, 12, 345, 65645, 77, 467, 1234]
print(noombahs)
noombahs.sort()
print("Sorted ", noombahs)



