# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    count = 0
    while count < elements:
        if len(arrA) == 0:
            merged_arr[count] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[count] = arrA[0]
            arrA.pop(0)
        elif arrA[0] >= arrB[0]:
            merged_arr[count] = arrB[0]
            arrB.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr[count] = arrA[0]
            arrA.pop(0)
        count += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # keep on splitting the array until the length is one
    if len(arr) < 2:
        return arr
    else:
        # (1) split up the array in half and have it be recursive
        # first half of the given array
        arr_one = merge_sort(arr[:len(arr)//2])
        # second half of the given array
        arr_two = merge_sort(arr[len(arr)//2:])

        # (2) run the helper function to merge
        return merge(arr_one, arr_two)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
