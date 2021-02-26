# Recursive Bucket Sort
import math

def bucket_sort(A):
    n = len(A)
    B = [[]] * (n - 1)
    for i in range(0, n - 1):
        B[math.floor(n * (A[i]))] = A[i]
    for i in range(0, n - 1):
        B[math.floor(n * (A[i]))].append(A[i])
    for i in range(0, len(B) - 1):
        insertion_sort(B[i])

    # concatenate B[0] and B[1] and B[2] . . .

def insertion_sort(A):
    for j in range(1, len(A)):
        i = j - 1
        key = A[j]

        while (i >= 0) and (A[i] > key):
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

A = ["grapes", "banana", "strawberry", "apple", "peach", "cherry"]
insertion_sort(A)
bucket_sort(A)
# print(A)
print(ord('c'))
# we need to do a recursive bucket sort, where each of the buckets have no more than 10 elements