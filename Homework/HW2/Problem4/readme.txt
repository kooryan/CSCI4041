Problem 4

Implementing the Johnson's algorithm was tricky, because the CLRS pseudocode had a lot of variable creation and management that
required to build a tree object, build a vertex object, and store all the distances in those, and then creating the weights and new weights
that could've been done much easier without creating all those helper objects. So I modified it and simplified the Dijkstra and Johnson algorithms
a lot, watering them down, but the performance should still be the same in big-O time.

For the Bellman-Ford algorithm, this was the most straightforward to implement based off of the CLRS pseudocode (the logical is mirrored identically).
What we do for all these Single-Source Shortest Paths algorithms is we need to initialize our single source first, making all the v.d infinity and then
setting the distance of our source (s.d) to 0. Then we looped through the vertices of our graph and relaxed each of the edges. Then we looped over each of
the edges again to see if there were any negative ones (because the main purpose of the Bellman-Ford algorithm in the Johnson's algorithm is to
get ensure there are no negative weights to prevent any negative cycles so we can run the Dijkstra algorithm on it). If the input graph contained a
negative cycle, then we'd stop there and the program would terminate after returning "Negative Cycle."

If there are no negative cycles in our graph then we would proceed by setting our h value to the delta(s, v) calculated from our Bellman-Ford algorithm (if you see
in my implementation, we don't actually return true but return the edges calculated by Bellman-Ford). Then what we did is initialize our array for
w-hat to compute new weights. The next lines then looped over all the vertices of the graph and then computed new weights to use for the Dijkstra algorithm.

After the new weights were computed, we would run the Dijkstra algorithm from each vertex and then add them to our new complete matrix D.

Running the Dijkstra algorithm was a little different from Problem 3, as instead of computing a single source shortest path, we needed to compute the shortest path
among all the vertices. I created a helper method to find the closest vertex or the neighbor that would run Dijkstra too, which then followed the same train of logic
in the relaxation stage of the algorithm and then just returned the distance after relaxation. This would be done when we loop over all the vertices of one row,
checking vertex 1 against all the other vertices, then checking vertex 2 against all the vertices and then getting the shortest path, which would then be used
in the Johnson algorithm to create our D matrix.