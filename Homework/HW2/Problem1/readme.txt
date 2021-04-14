Problem 1

This problem wasn't too hard. What I did was just create a Hash Table class with a constructor taking in a size parameters,
so I can create as many hash tables as I want of any size. Using the taken in size parameter I created buckets with a deque as my linked list
so when we add new keys the buckets could grow dynamically. I only implemented the "Search" and "Insert" algorithms for this solution
as we didn't ever require to delete anything (at least according to the prompt). Both implemented algorithms were adapted from the
CLRS pseudocode -- the hashing needed to be modified though since we aren't reading numerical values anymore, but strings, so I looked
around the textbook for any examples that hashed strings which I found in exercise 11.3-2 (where we summed up each of the characters then
just applied the division method on them).

The code is fairly straightforward for each algorithm, hashing the key, then finding its bucket.
Search just iterates over the bucket and finds the key it is looking for; when it is found it returns the key value and then the loop terminates.
The insert starts with defining our "obj" variable to either null or not. Then we hash and then check if obj is null. If it is,
then we simply append our key to the end of the bucket and the method terminates. Otherwise, we loop for the key and when we find it
we update the value.
