from os import *
from sys import *
from collections import *
from math import *

n = int(input())

for i in range(1,n+1):
    for j in range(n,0,-1):
        if (i==j):
            print("*",end="")
        else:
            print(j,end="")
    print()