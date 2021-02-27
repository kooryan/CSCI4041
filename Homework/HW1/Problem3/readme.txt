Problem 3

What we've done here is an implementation of Randomized Selection. It uses the "partition" part of the Quicksort algorithm
where we partition an array and we are looking for the "ith" smallest value (so when we've partitioned a given array, we need only
to look at one side of it). Again all of the code came directly from CLRS pseudocode as well as all its variable names and such.

There isn't really much to say here other than that I just converted their pseudocode into python.

We also import random in order to randomly choose our pivot during our rand_partition step.