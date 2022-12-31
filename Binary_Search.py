# Binary Search Algo


from sys import stdin


def binarySearch(arr, n, x) :
    start = 0 
    end = n
    mid = (start+end)//2
    while start<=end and mid<n:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid-1
        else:
            start = mid+1
        mid = (start+end)//2
    return -1
    #Your code goes here


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1