import sys
def count(arr,ele):
    c = 0
    for i in arr:
        if ele == i:
            c+=1
    return c

def duplicateNumber(arr, n) :
    for i in arr:
        c =count(arr,i)
        if  c == 2:
            return i
    #Your code goes here
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
    