

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def count_zeros(n):
    if n == 0:
        return 0
    # print(n)
    assum = count_zeros(n//10)
    # print(assum)
    if n%10==0:
        return 1+assum
    else:
        return assum



n = int(input())
if n ==0:
    print(1)
else:
    # print(n)
    print(count_zeros(n))