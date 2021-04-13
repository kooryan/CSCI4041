# Dijkstra's algorithm

import heapq
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
    S.append(math.inf)  # because if we do just -math.inf we are trying to compare an array with a number, which we don't want
    print(key)
    Decrease_Key(S, len(S) - 1, key)

def dijkstra(g, s, t):
    q = []
    d = {k: math.inf for k in g}
    p = {}
    path = []

    d[s] = 0
    q.append((0, s))

    while q:
        last_w, curr_v = Extract_Min(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                path.append(curr_v)
                Insert(q, (cand_w, n))

    path.append(t)
    final_path = list(dict.fromkeys(path))
    print(final_path)
  #  return str(d[t]) + ": " + path + str(t)

og = {}
og["0"] = [("1", math.inf), ("2", 4)]
og["1"] = [("0", 2), ("2", 7)]
og["2"] = [("0", math.inf), ("1", 3)]

print(dijkstra(og, "0", "1"))