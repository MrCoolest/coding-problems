
from os import *
from sys import *
from collections import *
from math import *

def number_of_possiblity(n):
    if n == 0:
        return 1
    if n<1:
        return 0
    one = number_of_possiblity(n-1)
    two = number_of_possiblity(n-2)
    three = number_of_possiblity(n-3)
    return one+two+three

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

print(number_of_possiblity(n))