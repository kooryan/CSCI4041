Problem 3

The CLRS pseudocode was a bit hard to follow for this one, so the general logic is mirrored, however the CLRS implementation takes in a source and
fights the shortest path to all vertexes. What we want is the shortest path from our source to a specified end point.

The initial set up for my implementation of Dijkstra's algorithm is basically the same as CLRS - we initialize the single source by setting all the
the v.d to infinity and then we set our source distance (s.d) to 0. Then after we append the G.V to our min priority queue Q. Then we looped over Q
and extract a vertex and its weight using our Extract-Min method from programming assignment 1. Then what we did is we looped through all the
vertices and relax the edges. If it was smaller than the original weight, then we would update v.d, add it to our path of vertexes that we would
need to go through to get to our end point, and inserted it into our min priority queue. Each time we add a vertex to our set we know for sure that
the distance is the shortest (u.d = delta(s, u)) which we proved in lecture.

Furthermore, this still chooses the "lightest" or "closest" vertex to add to our set, so it still maintains the property of being a greedy strategy as CLRS
outlined.