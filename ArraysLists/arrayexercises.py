sep = ('*' * 40)
my_array = ['element0', 'element1', 'element2', 'element3', 'element4', 'element5']

# to print elements and type of element
print(my_array[0], type(my_array[0]))
print(my_array[1])

# to traverse an array
print(sep)
for i in my_array:
    print(i)


# insert an element into an array
print(sep)
fruit = ['apple', 'banana', 'grape', 'lemon']
for f in fruit:
    print(f)
fruit.append('blueberry')
for f in fruit:
    print(f)
print(sep)