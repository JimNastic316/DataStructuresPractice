# Binary search example

def linear_search(list: list, target: object) -> int:
    """
    Searches for target, returns index where first found else -1
    Complexity: O(n) ["brute force" algo]
    :param list: list to search
    :param target: what trying to find
    :return: found item or -1 if not found
    """
    for i in range(len(list)):
        # once found, return index of first appearance and leave
        if list[i] == target:
            return i

    # list
    return -1


# Bubble sort
def selection_sort(list: list) -> None:
    """
    Sorts list in non-descending order
    Complexity: O(n**2)
    :param list: list to sort
    :return: None
    """
    for i in range(len(list) - 1):
        min_index = i

        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        temp = list[min_index]
        list[min_index] = list[i]
        list[i] = temp


def binary_search(list: list, target: object) -> int:
    """
    Searches for target, returns index where first found, else -1
    Complexity: O(log n)
    Precondition: list must be sorted in non-descending order
    :param list: list to be searched
    :param target: what trying to find
    :return: found item or -1 if not found
    """
    # set range of possible indices to entire list
    low = 0
    high = len(list) - 1

    while low <= high:

        # find the midpoint of possible indices to entire list:
        mid = (low + high) // 2

        # Since value is lower, if it's there will be left of mid
        if target < list[mid]:
            high = mid - 1
        # Since value is higher, if it's there will be right of mid
        elif target > list[mid]:
            low = mid + 1
        # Neither higher nor lower, it's a match - found
        else:
            return mid

    # All indices have been eliminated for consideration, target not found
    return -1


# Test input
some_list = [5, 2, 1, 8, 3, 12, 4, 7, 2, 6]
print("Initial list:", some_list)
selection_sort(some_list)
print("Sorted list: ", some_list)

target = int(input('\nEnter a value to search for: '))

result = binary_search(some_list, target)

if result >= 0:
    print(target, 'was found at index ', result)
else:
    print(target, 'was not found in the list')