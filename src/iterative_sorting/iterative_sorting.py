# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for index_pos in range(i, len(arr)):
            if arr[index_pos] < arr[smallest_index]:
                smallest_index = index_pos
        # TO-DO: swap
        value_switch = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = value_switch
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        is_switched = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                value_switch = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = value_switch
                is_switched = True
        if is_switched == False:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr