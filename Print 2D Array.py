from os import *
from sys import *
from collections import *
from math import *

size = input().split()

n,m = int(size[0]), int(size[1])


def printList(lis,n,m):
    times =n

    for i in lis:
        times = n
        while times>0:
            for j in i:
                print(j,end=" ")
            print()
            times-=1
        n-=1

lis = []
for i in range(n):
    line = [int(j)  for j in  input().split()]
    lis.append(line)

printList(lis,n,m)
