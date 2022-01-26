from static_array import StaticArray

class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Dynamic_Array_Iterator(object):
    def __init__(self,dyn_array):
        self.index = 0
        self.dyn_array = dyn_array

    def __iter__(self):
        return self

    # Use this for built-in iteration
    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        if self.index >= self.dyn_array.length():
            raise StopIteration

        value = self.dyn_array.get_at_index(self.index)

        self.index = self.index + 1
        return value

    # Use this when "manually" advancing an iterator
    def next(self):
        return self.__next__()


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
        return Dynamic_Array_Iterator(self)

    def __str__(self):
        return str(self.data)

    def append(self, val):
        # Will need to be amended to check if there is room and call method to expand array when necessary
        self.data[self.size] =  val
        self.size = self.size + 1

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def length(self) -> int:
        """
        Return number of elements stored in array
        """
        return self.size



# Create new instance of Dynamic_Array
my_list = Dynamic_Array()

# Build list with 10 items
for i in range(10):
    my_list.append(i)

# Iterate through list automagically via iterator
# Creates iterator behind the scenes and calls __next__()
for value in my_list:
    print(value)

print()

# Create two iterators that advance independent of each other
# Advance iterators "manually" by calling next()
itr1 = Dynamic_Array_Iterator(my_list)
itr1.next()

itr2 = Dynamic_Array_Iterator(my_list)
itr2.next()
itr2.next()
itr2.next()

print("Next item from itr1:",itr1.next())
print("Next item from itr2:",itr2.next())