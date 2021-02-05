# Merge sort with sentinels
import math

A = [3, 8, 6, 1, 7, 2, 5, 4]


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = A[p + i - 1]
    for j in range(0, n2):
        R[j] = A[q + j]

    L[n1] = float('inf') # sentinel values
    R[n2] = float('inf')

    i = 0
    j = 0

    for k in range(p - 1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergesort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)


mergesort(A, 1, len(A)) # needs to start at index 1 or else we miss the smallest value
print("The array is: ", A)