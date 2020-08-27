# Selection sort: O(n * n), in-place, stable/unstable

# By element's length, unstable
def selection_sort(lst):
    for i in range(len(lst) - 1):
        index = i

        for j in range(i + 1, len(lst)):
            if len(lst[j]) < len(lst[index]):
                index = j

        lst[i], lst[index] = lst[index], lst[i]

# By element's length, stable
def selection_sort_stable(lst):
    for i, el_i in enumerate(lst[:-1]):
        index = i

        for j, el_j in enumerate(lst[i + 1:], i + 1):
            if len(el_j) < len(lst[index]):
                index = j

        lst.insert(i, lst.pop(index))


arr = ['aaaa', 'bbbb', 'cccc', 'ddd', 'eee', 'ffff']
arr2 = arr[:]
selection_sort(arr)
selection_sort_stable(arr2)
print(arr)  # ['ddd', 'eee', 'cccc', 'aaaa', 'bbbb', 'ffff']
print(arr2)  # ['ddd', 'eee', 'aaaa', 'bbbb', 'cccc', 'ffff']
