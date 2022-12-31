def firstIndex(arr, x):
    # Please add your code here
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == x:
            return 1
        else:
            return -1
    
    if arr[0] == x:
        return 0
    assum =  firstIndex(arr[1:],x)
    # print(assum)
    if assum == -1:
        return assum 
    else :
        return assum+1
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
