# Given a sorted array of integers, return the two numbers such that \
# they add up to a specific target. You may assume that each input \
# would have exactly one solution, and you may not use the same element twice

array = [-5, -6, -3, -2, 0, 2, 4, 5, 7, 8, 14]
target = 15

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sum_method_1(array, target):
    """
    method: brute force
    """
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(array[i], array[j])
                return True
    return False


# Time Complexity: O(n)
# Space Complexity: O(n)
def sum_method_2(array, target):
    """
    method: using hash table
    """
    table = dict()
    for i in range(len(array)):
        if array[i] in table:
            print(table[array[i]], array[i])
            return True
        else:
            table[target - array[i]] = array[i]
    return False


# Time Complexity: O(n)
# Space Complexity: O(1)
def sum_method_3(array, target):
    """
    method: traversing from both sides
    """
    i = 0
    j = len(array) - 1

    while i <= j:
        if array[i] + array[j] == target:
            print(array[i], array[j])
            return True
        elif array[i] + array[j] < target:
            i += 1
        else:
            j -= 1
    return False



# verifying the methods
sum_method_1(array, target)
sum_method_2(array, target)
sum_method_3(array, target)
