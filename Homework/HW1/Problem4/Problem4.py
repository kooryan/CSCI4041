# Recursive Bucket Sort

def bucket_sort(A, start=0):
    n = len(A)
    B = []
    for i in range(ord('A'), ord('Z')):  # this should look from the start of the alphabet to the end
        B.append([])  # make number of buckets as the number of letters in the alphabet
        # ord('a') equals 97 and ord('A') equals 65

    if start == 0:
        for i in range(ord('A'), ord('Z')):
            for j in range(0, n):
                if A[j][0] == chr(i):
                    B[i - 65].append(A[j])  # we subtract by 65 because the unicode value of 'A' is 65 and we want our array to start from 0
    else:
        for i in range(ord('a'), ord('z')):
            for j in range(0, n):
                if A[j][start] == chr(i):
                    B[i - 97].append(A[j])  # same reason as above for why we subtract by 97

    for i in range(0, len(B) - 1):
        if len(B[i]) > 10:  # now we do a check here, if there are more than 10 elements in the bucket, then we recursively sort
            bucket_sort(B[i], start + 1)  # we have to make sure now that since we are looking at a bucket with all the same first characters, we look at the second characters now and go on
        else:  # otherwise that bucket is just sorted through a simple insertion sort
            insertion_sort(B[i])

    list = []
    for i in range(0, len(B) - 1):
        list.append(B[i])  # concatenate B[0] and B[1] and B[2] . . . once we're done we do a concatenation of all of our buckets, which should be in alphabetical order

    return list


def insertion_sort(A):
    for j in range(1, len(A)):
        i = j - 1
        key = A[j]

        while (i >= 0) and (A[i] > key):
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

input = open("input.txt", 'r').read()
output = open("output.txt", "w+")
List = input.split()

flat_list = []
for sublist in bucket_sort(List):  # Here we are flattening our array, so the 2D array becomes a 1D array and it's easy
    for item in sublist:
        output.write(item + " ")

output.close()