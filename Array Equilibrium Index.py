from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    a = 0
    for i in range(n):
        # b = sum (arr[i+1:])
        b =  sum(arr[i+1:])
        a += arr[i-1] or 0 
        # print(a,b)
        if a == b:
            return i
    return -1
    #Your code goes here




























#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1
