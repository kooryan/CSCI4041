# Floyd-Warshall algorithm


def floydWarshall(graph, new_vertexes, output=open("output.txt", "w+")):  # implementation of CLRS Floyd-Warshall algorithm
    n = len(graph)  # get the number of vertices before add the new vertex(es)
    V = n + len(new_vertexes)  # get the number of old vertices + new vertices
    D = [[0 for x in range(V)] for y in range(n)]  # create new empty adjacency matrix accounting for total vertices

    for i in range(n):
        for j in range(n):
            D[i][j] = graph[i][j]  # add our old vertices to our adjacency matrix

    for x in new_vertexes:
        D.append(x)  # add the new vertices to our adjacency matrix

    for a in range(len(D)):
        for b in range(len(D)):
            D[a][b] = D[b][a]  # since the graph is undirected, that means it will be symmetrical and thus we can find the edge weights when we add the new vertices

    # run the un added vertex matrix first normally, print out, if negative then the rest will be negative,
    # and then add the new vectors and continue running as normal
    hitOnce = False
    for k in range(V):  # Floyd-Warshall Algorithm, implementation taken from CRS - we loop over i, k, j in order to find a connection between i and j  --  Should still be O(|V|^3)
        for i in range(V):
            for j in range(V):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])  # Still takes O(1) time
            if i == n and not hitOnce:  # and not hitOnce:  here we are checking whether or not i (the starting node) is the size of our old adjacency matrix, and whether or not we've processed the loop already
                print(D)
                negativeCycle = False
                for x in range(n):  # going through our old matrix. This part is merely O(n) practically irrelevant to runtime
                    if D[x][x] < 0:  # taken from CLRS 25.2-6 -- if any of the diagonals are negative then it is a negative cycle
                        output.write("Negative cycle\n")
                        negativeCycle = True
                        break

                if not negativeCycle:  # if it is not a negative cycle then we loop through our old matrix and print out the re-weighted weights for each edge
                    for x in range(i):  # this part just loops through the matrix: O(n^2)
                        for y in range(i):
                            output.write(str(D[x][y]) + " ")
                        output.write("\n")
                hitOnce = True  # we don't want to process the loop again as we proceed to process the adjacency matrix with the old vertices so we set this to true

    for i in range(V):  # same logic as above, if any of the diagonals are negative then the new graph with the added vertices is a negative cycle
        if D[i][i] < 0:  # taken from CLRS 25.2-6
            output.write("Negative cycle")
            return

    for x in range(V):  # other wise we loop through our newly created matrix computed by the Floyd-Warshall algorithm
        for y in range(V):  # this part just loops through the matrix: O(V^2)
            output.write(str(D[x][y]) + " ")
        output.write("\n")
    return D


adj_matrix = []
new_vertexes = []
i = 0
n = 0
file = open('input.txt', 'r')
output = open("output.txt", "w+")

for line in file:
    line = line.split()
    if i == 0:
        n = len(line)  # the first line will be the length of the old matrix, after that we no longer want to update n
        i += 1  # so increment once so i == 0 is never true again
    if len(line) == n:  # if a line is equal to n that means it is part of the old matrix so add that as such
        temp = [int(num) for num in line]
        adj_matrix.append(temp)
    else:
        temp = [int(num) for num in line]  # else the line is part of the new added vertices so add as such
        new_vertexes.append(temp)

floydWarshall(adj_matrix, new_vertexes)

