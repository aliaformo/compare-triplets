#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compare_triplets(a, b):
    # Write your code here
    triplet_a = 0
    triplet_b = 0
    array_length = 3
    triplet_list = []
    
    for i in range(array_length):
        if a[i] > b[i]:
            triplet_a += 1
        elif a[i] < b[i]:
            triplet_b += 1
        else:
            pass            
                
    triplet_list.append(triplet_a)
    triplet_list.append(triplet_b)
    
    return triplet_list
    
    
print(compare_triplets([15,2,3], [3, 2, 1]))
print(compare_triplets([10, 11, 48], [19, 11, 49]))
    



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
