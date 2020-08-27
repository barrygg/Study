# Insertion sort: O(n ^ 2), stable, in-place
def insertion_sort(lst):
    for i, elem in enumerate(lst[1:], 1):
        j = i - 1
        key = elem
        while (j >= 0) and (lst[j] > key):
           lst[j + 1] = lst[j]
           j -= 1
        lst[j + 1] = key
