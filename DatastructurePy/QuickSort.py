import random

def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+sort(equal)+sort(greater)  # Just use the + operator to join lists
    else:
        return array

def sub_partition(array, start, end, idx_pivot):
    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')
    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1
    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, start,end):
    if end is None:
        end = len(array) - 1
    if end - start < 1:
        return 
    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    quicksort(array, start, i - 1) 
    quicksort(array, i + 1, end)
    return array

print(quicksort([12,4,5,6,7,3,1,15],0,None))
