def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found



# STRETCH: write an iterative implementation of Binary Search
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    # arr-1: gets the last element
    high = len(arr) - 1
    while low <= high:
        # this gets us number of half the list
        # // gets us integer not float
        middle_index = (low + high) // 2
    # gets us value at middle index in array
        my_guess = arr[middle_index]
        if target == my_guess:
            return middle_index
        if target < my_guess:
            high = middle_index - 1

        else:
            low = middle_index + 1

    return -1  # not found

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
