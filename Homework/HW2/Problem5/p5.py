# Floyd-Warshall algorithm


def floydWarshall(graph, new_vertexes, output=open("output.txt", "w+")):
    n = len(graph)
    V = n + len(new_vertexes)
    D = [[0 for x in range(V)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = graph[i][j]

    for x in new_vertexes:
        D.append(x)

    for a in range(len(D)):
        for b in range(len(D)):
            D[a][b] = D[b][a]
    # run the un added vertex matrix first normally, print out, if negative then the rest will be negative,
    # and then add the new vectors and continue running as "normal"? but how? add on to the new matrix?

    hitOnce = False
    for k in range(V):
        for i in range(V):
            for j in range(V):
                D[i][j] = min(D[i][j],
                                 D[i][k] + D[k][j])
            if k == n and not hitOnce:
                negativeCycle = False
                for x in range(n):
                    print(D[x][x])
                    print(D[x][x] < 0)
                    if D[x][x] < 0:  # taken from CLRS 25.2-6
                        output.write("Negative cycle\n")
                        negativeCycle = True
                        break

                if not negativeCycle:
                    for x in range(k):
                        for y in range(k):
                            output.write(str(D[x][y]) + " ")
                        output.write("\n")
                hitOnce = True

    for i in range(V):
        if D[i][i] < 0:  # taken from CLRS 25.2-6
            output.write("Negative cycle")
            return

    for x in range(V):
        for y in range(V):
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
        n = len(line)
        i += 1
    if len(line) == n:
        temp = [int(num) for num in line]
        adj_matrix.append(temp)
    else:
        temp = [int(num) for num in line]
        new_vertexes.append(temp)

floydWarshall(adj_matrix, new_vertexes)

