def power(x, n):
    # Please add your code here
    # print(n)
    if  n==0:
        return 1
    if n==1:
        return x
    smallPow = power(x, n//2)
    if n%2==0:
        return smallPow * smallPow
    else:
        return x*smallPow*smallPow

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
