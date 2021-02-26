# Heap priority queues
import math

# here we are building our max heap
def build_max_heap(A):
    for i in range(math.floor(len(A)/2), -1, -1):  # why go down to -1?
        max_heapify(A, i)


def max_heapify(A, i):
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l][1] > A[i][1]:
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
def Extract_Max(S):
    if len(S) < 1:
        print("heap underflow")
        return

    max = S[0]
    S[0] = S[len(S)-1]
    S.pop(len(S)-1) # this is our A.heapsize = A.heapsize - 1
    max_heapify(S, 0)
    return max


def Increase_Key(S, i, key):
    if key[1] < S[i][1]:
        print("new key cannot be smaller than current key")
        return

    S[i] = key
    while i > 0 and S[math.floor(i/2)][1] < S[i][1]:
        S[i], S[math.floor(i/2)] = S[math.floor(i/2)], S[i]
        i = math.floor(i/2)


def Insert(S, key):
    S.append(['inf', -math.inf]) # because if we do just -math.inf we are trying to compare an array with a number, which we don't want
    Increase_Key(S, len(S)-1, key)


def ptree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        ptree(A, i * 2 + 1, indent + 1)
        ptree(A, i * 2 + 2, indent + 1)

# file = open("input.txt", 'r')
List = []


Insert(List, ["Paul", 2])
Insert(List, ["Alan", 5])
print(Maximum(List))
Insert(List, ["Sue", 999])
Insert(List, ["Sally", 99])
Extract_Max(List)
print(Maximum(List))

print(List)

ptree(List)








