
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def pair_star(val):
    if len(val)==1:
        return val
    assum = pair_star(val[1:])
    if assum[0] == val[0]:
        return val[0]+'*'+assum
    else:
        return val[0]+assum

value = input()
print(pair_star(value))