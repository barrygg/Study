# Implementation of quick sort
# O(n * log n)
# Choosing the median of the first, middle and last element of the partition for the pivot (Sedgewick)
def partition(lst, start, end):
    tmp = [(lst[start], start),
           (lst[(start + end) // 2], (start + end) // 2),
           (lst[end], end)]
    tmp.sort()
    lst[start], lst[tmp[1][1]] = lst[tmp[1][1]], lst[start]
    left = start
    for i in range(start + 1, end + 1):
        if lst[i] > lst[start]:
            left += 1
            lst[i], lst[left] = lst[left], lst[i]

    lst[start], lst[left] = lst[left], lst[start]
    left_equal = left
    for k in range(left + 1, end + 1):
        if lst[k] == lst[left]:
            left_equal += 1
            lst[k], lst[left_equal] = lst[left_equal], lst[k]

    return left - 1, left_equal + 1


def quick_sort(lst, start, end):
    if start >= end:
        return

    less, great = partition(lst, start, end)
    quick_sort(lst, start, less)
    quick_sort(lst, great, end)



