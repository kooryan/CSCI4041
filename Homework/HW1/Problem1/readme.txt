Problem 1

This problem was fairly easy, as most of the solution came straight from the CLRS pseudocode.

What I've basically done is I implemented all the priority queues (Increase_Key, Maximum, Insert) however
I took them in as 2D arrays. Why? In order to store the name and their value. The input file gives us a
"node" in the form of ["name", value]. Thus, what this code has done essentially, is modified the pseudocode
slightly in order to accept 2D arrays, and basically compare each node against each other with their "value"
or the node[1] -- since I've set it up such that whenever input is read from the file, it always sets up each node
as node[0] being the name nad node[1] being the value.

If I was using Java, I would've used Scanner or BufferedReader to read input, but since I'm new to Python, my reader
is sort of "bootleg." I read each of the file input as an array (so each line is an array) that is essentially up to size 3
with the (1) the command (2) the name of the node (3) the value of the node.