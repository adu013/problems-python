# Sorting in ascending order \
# using Insertion Sort
def insertion_sort_via_swap(array):
    for i in range (1, len(array)):
        for j in range(i-1, -1, -1): # Starting from i-1 to 0 shifting by -1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                break
    return array


def insertion_sort_via_shift(array):
    for i in range (1, len(array)):
        current_value = array[i]
        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                array[j+1] = array[j]
            else:
                array[j+1] = current_value
    return array


# Validation
array = [4, 6, 24, 57, -4, -34, 73, 16, 8, 987, 3456, 34, -6736, 50]

x1 = insertion_sort_via_swap(array)
x2 = insertion_sort_via_shift(array)

print(x1)
print(x2)
