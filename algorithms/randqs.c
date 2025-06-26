/*
Randomized QuickSort
Runtime: Expected O(nlgn)
---

Implementation/Performance:
Honestly I think this algorithm is pretty simple to implement, 
and honestly it's expected asymptotically matches the version of 
QuickSort using Select, while probably doing much better  
in actual use cases.

Proof of Correctness:
This is one of the more intuitive POC's, it looks at the expected number 
of comparisons the algorithm makes. To do this, we find the probability of each unique
pair being compared, and add this up all unique pairs in order to get the number of 
comparisons.
*/
#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main() {
    int r = rand();
    printf("Random Number: %d", r);
    return 0;
}