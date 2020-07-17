def insertion_sort(array, reverse=False):
    if reverse:
        array = [-1*e for e in array]
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
    if reverse:
        array = [-1*e for e in array]
    return array
print(insertion_sort([5,2,4,6,1,3], reverse=True))
                