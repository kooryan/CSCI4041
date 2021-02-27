Problem 4

This one was pretty tough, as I did not finish it completely. The big flaw in my solution for this problem is that it is not able to handle
a set of names with more than ten of the same letter -- so it'll probably fail a lot of the hidden cases.

****Note: this explanation for my code here is for input with more than 10 names of the same letter****
While I was debugging the recursive bucket sort, and it most likely won't show on gradescope, for some reason, when I created the mini bucket
and sorted it, it would merge back into the larger array but for some reason it would return to its original unsorted state.

My approach here was to, on initialization, create 26 buckets each for a letter of the alphabet (because in the final array, I would be flattening it anyway
so any empty buckets would disappear). And looping through the alphabet and the input I would put each name into a bucket based on its first character
(thought it probably seems slow, I still believe it is O(N) -- as the first loop (going through the alphabet) is basically O(26) - O(1) and the second loop is O(n)
where we are just looping through the list of names). And basically from there, we would iterate over the buckets, and if it doesn't have more than 10 names, then it would
execute the insertion step and we are done. But if it does contain more than 10 characters, we would run ONLY that bucket (B[i]) through the bucket sort again.
However, I've spent the majority of my day trying to fix a bug that would result in the sorted mini bucket to become unsorted on merge with the larger array to no avail.

This was how I sought to tackle the problem but the implementation probably has some mistakes in the logic here and there that causes it to become "unsorted." Well, at least it doesn't
crash.

Finally, what we are doing is concatenating the lists at the end of the sort and returning it, where then I have another loop that "flattens" the array, so the 2D array becomes
a 1D array and we can iterate over it nicely.

