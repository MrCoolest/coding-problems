from os import *
from sys import *
from collections import *
from math import *


n = int(input())

i = 1
rows = n*2+1

while(i<=n):
    # print('*'*rows)
    for j in range(1, rows+1):
        if (j==i or j==(n+1) or j==(rows-i+1)):
            print("*",end="")
        else:
            print("0",end="")
    print()
    i+=1