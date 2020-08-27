# Merge sort implementations: recursive and loop
# O(n * log n), stable, not in-place
def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


# top-down
def merge_sort_recursive(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst) // 2
    left = merge_sort_recursive(lst[:middle])
    right = merge_sort_recursive(lst[middle:])

    return merge(left, right)

# bottom-up
def merge_sort_loop(lst):
    lst = [[i] for i in lst]
    while len(lst) > 1:
        lst.insert(0, merge(lst.pop(), lst.pop()))
    return lst[0]
