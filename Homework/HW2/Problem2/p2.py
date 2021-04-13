# Depth First Search and topological sort

from collections import defaultdict

adj_list = defaultdict(list)
topological_sorted_order = []


def dfs(courses, prereq):
    for dest, src in prereq:
        adj_list[src].append(dest)
    color = {k: "white" for k in courses}

    for vertex in courses:
        if color[vertex] == "white":
            dfs_visit(vertex, color)


def dfs_visit(node, color):
    color[node] = "gray"
    if node in adj_list:
        for neighbor in adj_list[node]:
            if color[neighbor] == "white":
                dfs_visit(neighbor, color)

    color[node] = "black"
    topological_sorted_order.append(node)


def topological_sort(courses, prerequisites):
    dfs(courses, prerequisites)
    return topological_sorted_order[::-1]


course = [1001, 1133, 2011, 1933, 4041]
prerequisites = [[1933, 1133], [4041, 1933], [4041, 2011]]

print(topological_sort(course, prerequisites))
