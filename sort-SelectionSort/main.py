# Sorting in ascending order \
# using Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# Validation

array = [567, 89786, 6, 24, 57, -4, -34, 73, 16, 8, 987, 3456, 34, -6736, 50]
x = selection_sort(array)
print(x)
