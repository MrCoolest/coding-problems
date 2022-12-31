from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def sum_of_digit(n):
    if n == 0:
        return n
    assum =  sum_of_digit(n//10)
    return (n%10)+assum


n = int(input())
print(sum_of_digit(n))