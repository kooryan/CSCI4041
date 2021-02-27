# Huffman Greedy Algorithm
import math


def build_min_heap(A):  # all of this follows the pseudo code from CLRS
    for i in range(math.floor(len(A) / 2), -1, -1):
        min_heapify(A, i)  # only difference between build_max_heap and this method is on this line


def min_heapify(A, i):  # all of this follows the pseudo code from CLRS
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l][1] < A[i][1]:  # logic change from max_heapify, where we are checking if the left child is less than the parent
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r][1] < A[smallest][1]:   # logic change from max_heapify, where we are checking if the right child is less than the parent
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def Extract_Min(Q):  # all of this follows the pseudo code from CLRS
    if len(Q) < 1:
        print("heap underflow")
        return

    min = Q[0]
    Q[0] = Q[len(Q) - 1]
    Q.pop(len(Q) - 1)  # this is our A.heapsize = A.heapsize - 1, pop() removing the last element of the list
    min_heapify(Q, 0)
    return min


def Decrease_Key(S, i, key):  # all of this follows the pseudo code from CLRS
    if key[1] > S[i][1]:  # we assume the new key is smaller than the current one
        print("new key cannot be larger than current key")
        return

    S[i] = key
    while i > 0 and S[math.floor(i / 2)][1] > S[i][1]:  # some logic is changed here -
        # instead of wanting our current index to be larger than the parent we want it to be smaller
        S[i], S[math.floor(i / 2)] = S[math.floor(i / 2)], S[i]
        i = math.floor(i / 2)


def Insert(S, key):
    S.append(['inf',
              math.inf])  # because if we do just -math.inf we are trying to compare an array with a number, which we don't want
    Decrease_Key(S, len(S) - 1, key)


def Huffman(C):
    n = len(C)  # C is assumed to be a set of "n" characters
    build_min_heap(C)  # building our list C as a min heap
    Q = C[:]  # setting our min priority Q to our min_heap C

    for i in range(0, n - 1):
        z = [0, 0]  # creating out new node z

        x = list(Extract_Min(Q))
        y = list(Extract_Min(Q))

        x.append(0)  # 0 - we are going in the left direction
        y.append(1)  # 1 - we are going in the right direction

        z[0] = x[0] + y[0]  # combining the letters
        z[1] = x[1] + y[1]  # combining the frequencies

        z.append(x)  # appending the left child onto our heap node to create the tree
        z.append(y)  # appending teh right child onto our heap node to create the tree

        Insert(Q, z)  # Insertion step

    return Extract_Min(Q)


def htree(L, code, output=open("output.txt", "w+")):  # construction of our binary tree
    for i in L:
        if isinstance(i, list):
            if len(i) == 5:  # we are at an internal node
                htree(i, code + str(i[4]))  # iterate recursively and make sure we know if we went left or right
            if len(i) == 3:  # we are at an external node, since if it is of length 3 it won't have children
                ncode = code + str(i[2])  # we are at a leaf so no recursion step here
                output.write(i[0] + ": " + ncode + "\n")


data = open("input.txt").read()

print(data)

frequency = {}
for i in data:  # looping through the dictionary and counting the frequency of each letter
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

frequency = list(frequency.items())  # converting our iterable to an array/table so we can get the frequencies of each character as a separate value from the letter

htree(Huffman(frequency), "")


