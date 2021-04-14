Problem 2

This problem, similarly to the last one, is basically a mirror implementation of the CLRS pseudo code.
Since this problem is a topological sort, and we want to hit the prerequisites first before the course requiring them,
we implement depth first search for this problem. Essentially, by the end we want an ordered list of vertices, where respect
the prerequisite conditions. The implementation and logic behind all of the algorithms are taken directly from the book and
explained through comments, so I'll just explain what we are doing in the main scheme of things. Depth First Search is intended
to check whether a certain vertex is reachable from another one. Topological sort on the other hand isn't looking for a specific
vertex, rather, it traverse's the graph in depth-first order (FILO) and adds a vertex to the head of a list after all of its prerequisite vertices
have been added to the list.

Thus, what we do is if the vertex is in the list already, we don't do any processing (since it's a black node). Otherwise, the vertex is not yet in the sorted list,
and thus we process all its neighbors first, coloring them gray and such, (this is again FILO) and then add them to the vertex list (blacken them).

Visually classes and their prerequisites are structured as such:

                                             5421
                                            /    \
                                          ...     4041
                                                  /  \
                                               1933  2011

and by using depth-first-search, we are processing the children first, and after the children have been process then we add the first processed vertex to ourl ist.