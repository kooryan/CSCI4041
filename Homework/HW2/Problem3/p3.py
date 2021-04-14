# Dijkstra's algorithm

import math


def min_heapify(A, i):  # all of this follows the pseudo code from CLRS
    l = 2 * i
    r = 2 * i + 1
    if l < len(A) and A[l] < A[i]:  # logic change from max_heapify, where we are checking if the left child is less than the parent
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:   # logic change from max_heapify, where we are checking if the right child is less than the parent
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
    if key[0] > S[i]:  # we assume the new key is smaller than the current one
        print("new key cannot be larger than current key")
        return

    S[i] = key
    while i > 0 and S[math.floor(i / 2)] > S[i]:  # some logic is changed here -
        # instead of wanting our current index to be larger than the parent we want it to be smaller
        S[i], S[math.floor(i / 2)] = S[math.floor(i / 2)], S[i]
        i = math.floor(i / 2)


def Insert(S, key):
    S.append(math.inf)
    Decrease_Key(S, len(S) - 1, key)


def dijkstra(G, s, t):  # implementation of Dijkstra in CLRS with some modifications -> we take in the graph, starting point, and end point, as opposed to graph, weight, and starting point
    q = []  # creation of our Q
    d = {k: math.inf for k in G}  # initialize single source, we set all the vertexes to edge distance infinity.
    path = []  # initialize an array to store each of the vertexes we traverse to get to our end point

    d[s] = 0  # set the starting vertex to s.d = 0
    q.append((0, s))  # adding G.V to Q

    while q:  # our while Q not null
        u, v = Extract_Min(q)  # here we split the u variable to take in the Extract_Min(Q)
        for n, n_w in G[v]:  # Looping through each vertex in G taking in a tuple (node, weight)
            if u + n_w < d[n]:  # Relaxation
                d[n] = u + n_w  # Relaxation - calculating our path distance
                path.append(v)  # add the vertex we just travelled to to our path list
                Insert(q, (u + n_w, n))  # insertion to Q
    path.append(t)  # adding our end node to the end of the path

    final_path = list(dict.fromkeys(path))  # formatting our path
    string_constructor = ""
    for i in final_path:  # converting our path list to a string to output
        string_constructor = string_constructor + i + " "
    return str(d[t]) + ": " + string_constructor  # our path distance


file = open("input.txt", 'r')
output = open("output.txt", "w+")

s, t = file.readline().split()
matrix = {}

i = 0
for line in file:  # reading in the file
    line = line.split()
    temp_array = []
    for j in range(len(line)):
        if i != j:
            temp_array.append((str(j), int(line[j])))  # taking in the vertex as a string and its weight as an int
            matrix[str(i)] = temp_array # add it to our matrix of nodes
    i += 1


output.write(dijkstra(matrix, str(s), str(t)))

output.close()

