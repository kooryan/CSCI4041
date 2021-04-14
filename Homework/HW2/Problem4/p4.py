# Johnson Algorithm

import math
from collections import defaultdict


def bellmanford(G, edges):  # implementation of Bellman-Ford algorithm based on CLRS
    d = [math.inf] * (len(G) + 1)  # initialize single source
    d[len(G)] = 0

    for i in range(len(G)):
        for (s, t, w) in edges:  # s - starting point, t - end point, w - edge weight
            if d[s] + w < d[t]:  # Relaxation
                d[t] = d[s] + w
        for (s, t, w) in edges:  # looping over each edge
            if d[s] + w < d[t]:  # If true this is a negative cycle
                return False
        return d[0:len(G)]  # return h(v) or basically returning True here


# helper method - construction of a shortest path tree, adding vertices with the smallest distance from the source first
def find_neighbor(d, spt):
    global neighbor

    minimum = math.inf  # setting our minimum distance to infinity as a base
    for v in range(len(d)):  # looping over vertices
        if d[v] < minimum and spt[v] == False:  # checks to see if we have already visited this vertex yet
            minimum = d[v]  # update minimum
            neighbor = v  # set our neighbor
            spt[v] = True  # that vertex is now visited so set it to true
    return neighbor


def dijkstra(G, s):  # implementation of Dijkstra - different from Q4 as we need to find All Shortest Paths now
    d = [math.inf] * len(G)  # initialize single source
    d[s] = 0

    spt = defaultdict(lambda: False)  # tree set of whether we have visited a vertex yet or not

    for count in range(len(G)):  # looping through each vertex in the graph
        u = find_neighbor(d, spt)  # choose the vertex with the small distance from the source or the "neighbor"

        for v in range(len(graph)):  # Relaxation
            if d[v] > (d[u] + G[u][v]):
                d[v] = (d[u] + G[u][v])
    # we didn't create a min priority queue because we are going through each vertex one by one - checking vertex 1 against all the other vertices, then checking vertex 2 against all the vertices
    return d  # runtime should still be the same as the implementation in CLRS


# Modified CLRS implementation - was a little difficult trying to implement after the 7th line of pseudocode
def johnson(G):
    edges = []  # computation of G'.E
    for i in range(len(G)):  # Creating edges to use for Bellman-Ford algorithm
        for j in range(len(G[i])):
            if G[i][j] != 0:
                edges.append([i, j, G[i][j]])

    for i in range(len(G)):  # Creating out super vertex
        edges.append([len(G), i, 0])

    if not bellmanford(G, edges):  # using Bellman-Ford to check if the graph is a negative cycle, don't want to proceed
        return "Negative cycle"
    else:
        h = bellmanford(G, edges)  # defining our h(v) calculated from Bellman-Ford

        ww = [[0 for x in range(len(G))]
              for y in range(len(G))]  # initializing w-hat from CLRS

        for i in range(len(G)):
            for j in range(len(G[i])):
                ww[i][j] = (G[i][j] + h[i] - h[j])  # computing the new weights from h(v) computed through the Bellman-Ford algorithm

        D = []  # creating a new matrix
        for v in range(len(G)):  # looping over vertices and running Dijkstra's on them to find all the shortest paths
            D.append(dijkstra(ww, v))
        return D  # return our new adjacency matrix of updated values


output = open("output.txt", "w+")

with open('input.txt', 'r') as f:
    graph = [[int(num) for num in line.split()] for line in f]
graph = johnson(graph)

if graph == "Negative cycle":
    output.write(graph)
else:
    for i in graph:
        for j in i:
            output.write(str(j) + " ")
        output.write("\n")

output.close()
