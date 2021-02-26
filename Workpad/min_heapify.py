import math

def build_min_heap(A):
    for i in range(math.floor(len(A)/2), -1, -1):  # why go down to -1?
        min_heapify(A, i)

def min_heapify(A, i):
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def ptree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        ptree(A, i * 2 + 1, indent + 1)
        ptree(A, i * 2 + 2, indent + 1)

array = [5, 13, 2, 27, 7, 17, 20, 8, 4]
build_min_heap(array)
print(array)
ptree(array)