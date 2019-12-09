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
    # create a counting arr based on length of inputted array
    count_arr = list(range(0, len(arr)))
    # set values of counting arr to zero
    for counter in count_arr:
        count_arr[counter] = 0
    # sort through arr by updating count arr
    for i in arr:
        count_arr[i] += 1
    # update arr by going through the count arr values
    index = 0
    stepper = 0
    for counter in count_arr:
        while counter > 0:
            arr[index] = stepper
            index += 1
            counter -= 1
        stepper += 1
    
    return arr