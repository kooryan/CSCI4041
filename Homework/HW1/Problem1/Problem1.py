# Heap priority queues
import math

# here we are building our max heap
def build_max_heap(A):  # all of this follows the pseudo code from CLRS
    for i in range(math.floor(len(A)/2), -1, -1):
        max_heapify(A, i)


def max_heapify(A, i):  # all of this follows the pseudo code from CLRS, where A is the array and i is the current node
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l][1] > A[i][1]:  # we are using a two-dimensional array, where its constituents is another array composed of [name, value]
        largest = l
    else:
        largest = i
    if r < len(A) and A[r][1] > A[largest][1]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


# since the array should be in (max) heap structure, we can just take the root and return it, which should be our max
def Maximum(S):
    return S[0][0]


# getting the max from the root, since our list should be a max heap
def Extract_Max(S):  # all of this follows the pseudo code from CLRS
    if len(S) < 1:  # if our heap is less than length 1 we have no heap
        print("heap underflow")
        return

    max = S[0]
    S[0] = S[len(S)-1]
    S.pop(len(S)-1)  # this is our A.heapsize = A.heapsize - 1, pop() removing the last element of the list
    max_heapify(S, 0)
    return max


def Increase_Key(S, i, key):  # all of this follows the pseudo code from CLRS
    if key[1] < S[i][1]:  # we assume here that the new key is at least as big as the current key
        print("new key cannot be smaller than current key")
        return

    S[i] = key
    while i > 0 and S[math.floor(i/2)][1] < S[i][1]:  # we want the current index i to be larger than our parent node
        S[i], S[math.floor(i/2)] = S[math.floor(i/2)], S[i]
        i = math.floor(i/2)


def Insert(S, key):  # all of this follows the pseudo code from CLRS
    S.append(['inf', -math.inf])  # because if we do just -math.inf we are trying to compare an array with a number, which we don't want
    Increase_Key(S, len(S)-1, key)


List = []

file = open("input.txt", 'r')
output = open("output.txt", "w+")

for line in file:
    line = line.split()
    if line[0] == "insert":
        Insert(List, [line[1], int(line[2])])  # our insert command
    elif line[0] == "max":
        output.write(Maximum(List) + "\n")  # formatting to make it look nice
        print(Maximum(List) + "\n")
    elif line[0] == "extract":
        Extract_Max(List)
    else:
        for i in List:
            output.write(i[0] + " ")  # we want the first value which is the name

output.close()