#  The algorithm works in O(log n)

# Iterative implementations of binary search
def binary_search_iterative(elements, target):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


# Recursive implementation of binary search
def binary_search_recursive(elements, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if elements[middle] == target:
        return middle
    elif target < elements[middle]:
        return binary_search_recursive(elements, target, left, middle - 1)
    else:
        return binary_search_recursive(elements, target, middle + 1, right)
