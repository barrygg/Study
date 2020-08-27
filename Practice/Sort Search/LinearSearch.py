# Linear search: the worst case — O(n)
def linear_search(elements, target):
    index = -1

    for i, elem in enumerate(elements):
        if elem == target:
            index = i
            break

    return index
