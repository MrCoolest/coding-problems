from sys import setrecursionlimit


def lastIndex(arr, x, si):
    # Please add your code here
    if len(arr) == si:
        return -1
    assum = lastIndex(arr, x, si+1)
    if assum == -1 and arr[si] == x:
        return si
    else:
        return assum
# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(lastIndex(arr, x, 0))
