#!/bin/python3
'''
https://www.hackerrank.com/challenges/is-fibo/problem
'''

import math
import os
import random
import re
import sys

#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isFibo(n):
    if math.sqrt((5*n**2 - 4)) % 1 == 0 or math.sqrt((5*n**2 + 4)) % 1 == 0:
        return "IsFibo"
    else:
        return "IsNotFibo" 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
