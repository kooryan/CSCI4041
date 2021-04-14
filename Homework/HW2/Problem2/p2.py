# Depth First Search and topological sort

from collections import defaultdict

adj_list = defaultdict(list)  # creation of our adjacency list so it can be accessed anywhere
topological_sorted_order = []   # creation of our topological sort array so it can be accessed anywhere


def dfs(courses, prereq):  # this is our implementation of the depth-first-search algorithm
    for dest, src in prereq:  # the prerequisites will have the course: requisite thus we make a tuple out of it
        adj_list[src].append(dest)  # our tuple with (destination, source) or (prerequisite, course) is appended to our adjacency list
    color = {k: "white" for k in courses}  # then what we do is we have a dictionary of colors to keep track, starting with all of our nodes as white

    for vertex in courses:  # implementation of CLRS pseudo code
        if color[vertex] == "white":  # if the node is white, then we call dfs-visit
            dfs_visit(vertex, color)


def dfs_visit(node, color):  # implementation of CLRS dfs-visit
    color[node] = "gray"  # first we color the node gray since we are on it now - or it's been "discovered"
    if node in adj_list:  # A check if the node is in the adjacency list
        for neighbor in adj_list[node]:  # loop through the adjacency list - we are exploring the edges here
            if color[neighbor] == "white":  # if the node is white, then we visit it and color it gray
                dfs_visit(neighbor, color)  # here is the FILO part of DFS - we check the most last node and do something with it

    color[node] = "black"  # once we are done with the node we blacken it
    topological_sorted_order.append(node)  # here we are executing topological sort from the CLRS pseudo code - we add the first nodes to be colored black at the front of a list


def topological_sort(courses, prerequisites):  # implementation of topological sort from CLRS
    dfs(courses, prerequisites)  # DFS internally has all the topological sort steps, call dfs -> once a vertex is finished insert into the front of a list
    return topological_sorted_order[::-1]  # -> then we return the list of vertices; since sorted vertices return in reverse order, we just reverse that to get the sorting order we want


file = open("input.txt", 'r')
output = open("output.txt", "w+")

course = []
prerequisites = []
for line in file:
    line = line.split(":")
    line[1] = line[1].split()
    course.append(int(line[0]))
    for i in line[1]:
        prerequisites.append([int(line[0]), int(i)])  # our nodes have tuple format (string, int)


for i in topological_sort(course, prerequisites):
    output.write(str(i) + " ")

output.close()
