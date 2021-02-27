Problem 2

This problem was tough. The toughest part was actually creating the binary tree in order to present our
Huffman code. Basically the implementation, again, follows CLRS's pseudocode, with modifications to priority queue,
instead of it being "max" it is now min. The main difficulty, again (well, at least for me), is creating nodes and
creating our binary tree from the bottom up. What I've done basically, is creating a nested array, for example:
['acbfed', 100, ['a', 45, 0], ['cbfed', 55, ['cb', 25, ['c', 12, 0], ['b', 13, 1], 0], ['fed', 30, ['fe', 14, ['f', 5, 0], ['e', 9, 1], 0], ['d', 16, 1], 1], 1]]

where if it contains 5 values, it is a internal node holding its (1) "combined characters" (2) combined frequency (3/4) right and left children (5) the direction it is in

The same basically goes for nodes with 3 values, which are our leaf nodes, holding its (1) character (2) frequency (3) its direction from its parent node.
Essentially we are looking at the "code" or representation of the children from the perspective of the parent node.

Then we recursively iterate over this tree that we've created (using my htree function) where we look at the direction of each node going down from the root.
While we are going down from the parent node, we are remembering the direction we went into until we arrive at a leaf node where
then we assign the code we've created to that character, and then store it into an array.