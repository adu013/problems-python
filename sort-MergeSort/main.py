# Sorting in ascending order \
# using Merge Sort
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid_index = int(len(array)/2)
    left = merge_sort(array[:mid_index])
    right = merge_sort(array[mid_index:])
    return merge(left, right)


# Validation

# x = merge([1,4,5,7], [2,4,6])
# print(x)

array = [4, 6, 24, 57, -4, -34, 73, 16, 8, 987, 3456, 34, -6736, 50]
x = merge_sort(array)
print(x)
