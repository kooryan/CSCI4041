# Randomized Selection
import random


def rand_select(A, p, r, i):  # implementing random selection from CLRS
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


def rand_partition(A, p, r):  # implementing random partition from CLRS
    i = random.choice([p, r])  # randomly selects a number from a given array
    A[r], A[i] = A[i], A[r]  # swapping to start partition
    return partition(A, p, r)  # over randomization, we call partition


def partition(A, p, r):  # partition step taken from Quicksort -- pseudocode is also CLRS
    i = p - 1  # index of the smaller element
    pivot = A[r]  # pivot

    for j in range(p, r):
        if A[j] <= pivot:   # if the current element is smaller than the pivot
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


input = open("input.txt").read()
output = open("output.txt", "w+")

List = ([int(n) for n in input.split()])  # looping over the input file, splitting it, and taking each value as an integer
output.write(str(rand_select(List, 1, len(List)-1, List[0])))  # calling rand select and writing it to an output file

output.close()
