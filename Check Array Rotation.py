
from sys import stdin

def arrayRotateCheck(arr, n):
    ans = 0
    for i in range(1,n):
        if arr[ans]>arr[i]:
            ans = i
    return ans
    #Your code goes here






#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1