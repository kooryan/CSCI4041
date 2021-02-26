# Huffman Greedy Algorithm
import math

def build_min_heap(A):
    for i in range(math.floor(len(A)/2), -1, -1):  # why go down to -1?
        min_heapify(A, i)

def min_heapify(A, i):
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l][1] < A[i][1]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r][1] < A[smallest][1]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def Extract_Min(Q):
    if len(Q) < 1:
        print("heap underflow")
        return

    min = Q[0]
    Q[0] = Q[len(Q) - 1]
    Q.pop(len(Q) - 1)  # this is our A.heapsize = A.heapsize - 1
    min_heapify(Q, 0)
    return min

def Decrease_Key(S, i, key):
    if key[1] > S[i][1]:
        print("new key cannot be smaller than current key")
        return

    S[i] = key
    while i > 0 and S[math.floor(i/2)][1] > S[i][1]:
        S[i], S[math.floor(i/2)] = S[math.floor(i/2)], S[i]
        i = math.floor(i/2)

def Insert(S, key):
    S.append(['inf', math.inf]) # because if we do just -math.inf we are trying to compare an array with a number, which we don't want
    Decrease_Key(S, len(S) - 1, key)


def Huffman(C):
    n = len(C) # C is assumed to be a set of "n" characters
    build_min_heap(C) # building our list C as a min heap
    Q = C # setting our min priority Q to our min_heap C

    for i in range(0, n - 1):
        z = [0, 0] # creating out new node z
        x = Extract_Min(Q)
        y = Extract_Min(Q)
        z[0] = x[0] + y[0]  # combining the letters
        z[1] = x[1] + y[1]  # combining the frequencies\
        Insert(Q, z)
        print(Q)

    return Extract_Min(Q)


data = "ffffeeeeeeeeefccccccccccccbbbbbbbbbbbbbddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

frequency = {}
for i in data:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

frequency = list(frequency.items())
print(frequency)

print(Huffman(frequency))


# array = [5, 13, 2, 27, 7, 17, 20, 8, 4]
# build_min_heap(array)
# print()
