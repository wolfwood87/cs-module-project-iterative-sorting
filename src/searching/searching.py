def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid_point = (low + high) //2
        if arr[mid_point] == target:
            return mid_point
        elif arr[mid_point] > target:
            high = mid_point - 1
        else:
            low = mid_point + 1

    return -1  # not found
