#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n)
Linear- Processing time is linear in relation to size of input, the bigger the input -> longer it takes to complete
n is constant and there is just one loop.

b)

O(n log n)
As input increases the runtime will grow at a slightly faster rate.


c)

O(n)
Linear- Processing time is linear in relation to size of input, the bigger the input -> longer it takes to complete
n or bunnies is constent and no loop

## Exercise II

Binary search- divide and conquer

1. n-story building/2 - take the number of stories and divide in half to find the middle floor.
    2. Drop the egg
        if - it breaks - we can eliminate all the floors above the halfway point + current floor
        if - it doesn't break - we can eliminate all the floors below keep the current floor as this floor still qualifies.
    repeat these steps -> current floor/2 -> if breaks eliminate floors above if doesnt eliminate floors below etc. 
dividing search in half each time
O(log n)- halving the list each time
