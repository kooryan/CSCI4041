Problem 5

Instead of modifying the Johnson Algorithm, I found it more practical to just use the Floyd-Warshall algorithm since it's much easier to modify
for this specific case, and it's performance/runtime is about the same anyway so we it'd be "as efficient" or more than what the prompt
stated what the runtime should be: runtime(# of old vertex) + runtime(# of new vertex) = runtime(# total vertex).

My implementation of the Floyd-Warshall algorithm follows the same train of logic as the pseudocode in CLRS, with some modifications
to them in terms of processing the adjacency matrices, since we now need to account for the new condition where we are adding new
vertices.

My implementation takes the old matrix constraints first and computes the Floyd-Warshall algorithm on it. Then it returns the current matrix
within the bounds of the old adjacency matrix, and that is essentially what the matrix is before we add the new vertices. Then the algorithm
proceeds in taking into account the newly added vertices and may modify the shortest existing paths as such.

Now comparing the efficiency of this compared to the prompts definition of "efficient" the Johnson algorithm takes around
O(V^2log V + VE) vs. the runtime of my implementation of the Floyd-Warshall algorithm which should still be O(|V|^3) as the main
processing that is going on is in the triple loop (finding a connection between i and j using the intermediate vertex k).

All other logic takes O(1), O(n), or once O(n^2) which is just traversing our matrix and is practically negligible to runtime.