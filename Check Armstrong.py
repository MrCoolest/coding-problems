from os import *
from sys import *
from collections import *
from math import *


def is_armstrong(n):
    og = str(n)
    for i in og:
        sum = 0
        for j in og:
            sum+=int(j)**int(i)
        
        if sum == n:
            return True
    return False

n = int(input())

if (is_armstrong(n)):
    print('true')
else:
    print('false')
