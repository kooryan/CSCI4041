# Insertion Sort

A = [5, 2, 8, 4, 6, 1, 3, 7]

count = 0

for j in range(1, len(A)):
    i = j - 1
    key = A[j]

    while (i >= 0) and (A[i] > key):
        A[i + 1] = A[i]
        i = i - 1
        count = count + 1

    A[i + 1] = key

print("The array is: ", A)