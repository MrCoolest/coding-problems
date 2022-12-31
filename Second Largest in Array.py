# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin

def findgretest(arr,n):
    great = arr[0]
    for i in range(1,n):
        if great<arr[i]:
            great=arr[i]
    return great

# def reverse_insertion_sorting(arr, n):
#     for i in range(1,n):
#         for j in range(i-1,-1,-1):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


def secondLargestElement(arr, n):
    second = -2147483648
    if n>0:
        # reverse_insertion_sorting(arr,n)
        largest = findgretest(arr,n)
        
        for i in range(0,n):
            if arr[i]!=largest:
                second = max(second,arr[i])
    return second


    #Your code goes here




#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1