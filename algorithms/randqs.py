"""
Randomized QuickSort
Runtime: Expected O(nlgn)
---

Implementation/Performance:
Honestly I think this algorithm is pretty simple to implement, 
and honestly it's expected asymptotically matches the version of 
QuickSort using Select, while probably doing much better  
in actual use cases.

POC:
The POC for this relatively simply, all we need to do is find the expected
number of comparisons the algorithm makes, then we can use an indicator random variables 
to denote whether any pair of elements are compared in the sorting algorithm. 
To do this, we need to find the probability of two elements being compared.
"""

from random import randint

def randqs_helper(array: list, pivot_index: int):
    # Base Case
    if (len(array) <= 1):
        return array
    
    
    point = array[pivot_index]
    # This is misleadingly titled lol
    left_half = []
    right_half = []
    
    for index in range(0, len(array)):
        if index != pivot_index:
            if array[index] <= point:
                left_half.append(array[index])
            else:
                right_half.append(array[index])
    
    # This case breaks random.randint
    if (len(left_half) <= 1):
        left_sorted = randqs_helper(left_half, 0)
    else:
        left_sorted = randqs_helper(left_half, randint(0, len(left_half)-1))


    # This case breaks random.randint
    if (len(right_half) <= 1):
        right_sorted = randqs_helper(right_half, 0)
    else:
        right_sorted = randqs_helper(right_half, randint(0, len(right_half)-1))

    left_sorted.append(point)
    return left_sorted + right_sorted


def randqs(array: list):
    # Also need to handle singletons in the main implementation
    if len(array) <= 1:
        return array
    
    return randqs_helper(array, randint(0, len(array)-1))


# Sample Cases
sorted = [1, 2, 3, 4, 5]
singleton = [1]
empty_array = []
mixed_bag = [randint(0, 100) for i in range(0, 21)] # 20 items

print("Already Sorted ...")
print(f"{sorted} -> {randqs(sorted)}")

print("Singleton ...")
print(f"{singleton} -> {randqs(singleton)}")

print("Empty Array ...")
print(f"{empty_array} -> {randqs(empty_array)}")

print("Mixed Bag ...")
print(f"{mixed_bag} -> {randqs(mixed_bag)}")