# Bubble sort: O(n ^ 2), stable, in-place
def bubble_sort(a):
    i = 0
    t = True
    while t:
        t = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                t = True
        i += 1
