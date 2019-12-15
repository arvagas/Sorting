# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    count = 0
    for i in arr:
        if i == target:
            return count
        else:
            count += 1
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return -1 # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high >= low:
        middle = (low+high)//2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if high >= low:
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search_recursive(arr, target, low, middle - 1)
        elif arr[middle] < target:
            return binary_search_recursive(arr, target, middle + 1, high)
    else:
        return -1
    