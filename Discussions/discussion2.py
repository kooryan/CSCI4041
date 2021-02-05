# Merge sort
import math

A = [3, 8, 6, 1, 7, 2, 5, 4]


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1: # fill in the remaining values
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, p, r):
    if p < r:
        q = math.floor((p + r - 1) / 2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)


mergesort(A, 0, len(A) - 1)
print("The array is: ", A)
