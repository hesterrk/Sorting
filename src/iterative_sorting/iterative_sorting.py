# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through all elements
    # 0 is the starting index
    for i in range(0, len(arr)):
        # Initially, the first element is considered the minimum and compared with other elements
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if (arr[j] < arr[smallest_index]):
                smallest_index = j

            # where we had current --> smallest (on right side) which was [3, 2] these get swapped, to smallest -> current (left) to 2, 3
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    # This condition is true if there were swaps in the previous iteration
    # If there we no swaps made (last time) then the list is sorted
    while swapped:
        # change it to false initially before for loop
        swapped = False
        # first index to second last index, as nothing to compare the last element with (no number on its right side)
        for i in range(len(arr) - 1):
            # Comparing neighbours: if current item is bigger than next one condition
            if arr[i] > arr[i + 1]:
                # swap the numbers
                # arr[i] gets assigned the new value of arr[i+1] and arr[i+1] gets assigned the value of arr[i]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # change to true so the while loop runs again!
                swapped = True

    return arr


bubble_sort([5, 2, 1, 7])


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
