# Randomized Selection
import random

def rand_select(A, p, r, i):
    if p == r:
        return A[p]
    q = rand_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return rand_select(A, p, q - 1, i)
    else:
        return rand_select(A, q + 1, r, i - k)

def rand_partition(A, p, r):
    i = random.choice([p, r])
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r):
    i = p - 1  # index of smaller element
    pivot = A[r]  # pivot

    for j in range(p, r):
        # If current element is smaller than the pivot
        if A[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)

# fills our list
List = [4, 5, 8, 2, 4, 7, 5, 0, 8, 2, 3, 9, 23, 48, -12, 49]

# input = open("input.txt")

# for i in range

print(rand_select(List, 0, len(List)-1, 3))