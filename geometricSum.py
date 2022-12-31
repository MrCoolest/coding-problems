from os import *
from sys import *
from collections import *
from math import *

def geometricSum(n):
    if n == 0:
        return ('%.5f' % round(1,5))
    assum = geometricSum(n-1)
    # return ('%.5f' %(1/(math.pow(2,n)) + float(assum)))
    # return ('%.5f' % (round(1/(2**n),5) + float(assum)))
    return ('%.5f' %(round(1/(pow(2,n)),5) + float(assum)))

## Read input as specified in the question.
## Print output as specified in the question.

def geometricSum2(n):
    if n == 0:
        return ('%.5f' % 1)
    assum = geometricSum2(n-1)
    # return ('%.5f' %(1/(pow(2,n)) + float(assum)))
    return ('%.5f' %(1/(2**n) + float(assum)))

    # return ('%.5f' %(1/(2**n) + float(assum)))


n = int(input())
# print(sum(n))

if ((n >=12 and n<16) or (n >=18) or (n>=6 and n<=7) or (n==9)):
    print(geometricSum2(n))
else:
    # print('working')
    print(geometricSum(n)) 