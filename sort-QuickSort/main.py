# Sorting in ascending order \
# using Quick Sort
def get_pivot(arr, low, hi):
    mid = (hi + low) // 2
    pivot = hi

    if arr[low] < arr[mid]:
        if arr[mid] < arr[hi]:
            pivot = mid
    elif arr[low] < arr[hi]:
        pivot = low

    return pivot


def partition(arr, low, hi):
    pivot_index = get_pivot(arr, low, hi)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, hi+1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border],  arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    return border


def _quick_sort(arr, low, hi):
    if low < hi:
        p = partition(arr, low, hi)
        _quick_sort(arr, low, p-1)
        _quick_sort(arr, p+1, hi)


def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)
    print(array)


# validation
# array = [4, 6, 24, 57, -4, -34, 73, 16, 8, 987, 3456, 34, -6736, 50]
array = [6, 3, 7, 1, 4, 5, 2]
quick_sort(array)
