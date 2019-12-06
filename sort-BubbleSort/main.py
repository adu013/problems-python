# Sorting in ascending order \
# using Bubble Sort
array = [2, 5, 3, 7, 8, 1, 8, 9, 4, 6]

def _swap(a, b):
    a, b = b, a
    return a, b

def sort(array):
    for i in range(len(array)):
        for j in range((len(array)-1)):
            if array[j] > array[j+1]:
                array[j], array[j+1] = _swap(array[j], array[j+1])
    print(array)
    return

# Validation
sort(array)
