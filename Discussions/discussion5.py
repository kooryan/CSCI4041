# Max-heapify & Heap sort
import math

array = [5, 13, 2, 27, 7, 17, 20, 8, 4]


def build_max_heap(A):
    for i in range(math.floor(len(A)/2), -1, -1):  # why go down to -1?
        max_heapify(A, i)


def max_heapify(A, i):
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def ptree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        ptree(A, i * 2 + 1, indent + 1)
        ptree(A, i * 2 + 2, indent + 1)


build_max_heap(array)
ptree(array)

print(array)

