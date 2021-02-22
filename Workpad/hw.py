A = [3, 2, 1]

i = 1
count = 1
while i < len(A):
    x = A[i]
    j = i - 1
    count += 3
    while j >= 0 and A[j] > x:
        A[j + 1] = A[j]
        j -= 1
        count += 3
    A[j+1] = x
    i += 1
    count += 3
count += 1

print(count)
print(A)
