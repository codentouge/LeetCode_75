#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = neg = naught = 0
    LEN = len(arr)
    
    
    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        else:
            naught += 1
        
            
    print(f"{float(pos)/LEN:.6f}\n{float(neg)/LEN:.6f}\n{float(naught)/LEN:.6f}")
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
