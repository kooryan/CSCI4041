# Insertion Sort

A = [4, 5, 8, 2, 4, 7, 5, 0, 8, 2, 3, 9, 23, 48, -12, 49]

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