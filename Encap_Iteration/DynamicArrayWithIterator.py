from static_array import StaticArray, StaticArrayException

class Dynamic_Array:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self.size = 0
        self.capacity = 10
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __iter__(self):
        """
        Create iterator for loop
        """
        self.index = 0

        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        try:
            value = self.data[self.index]
        except StaticArrayException:
            raise StopIteration

        self.index = self.index + 1
        return value

    def __str__(self):
        return str(self.data)

    def append(self, val):
        # Will need to be amended to check if there is room and call method to expand array when necessary
        self.data[self.size] =  val
        self.size = self.size + 1


# Create new instance of Dynamic_Array
my_list = Dynamic_Array()

# Build list with 10 items
for i in range(10):
    my_list.append(i)

# Iterate through list automagically via iterator
for value in my_list:
    print(value)

print(my_list)