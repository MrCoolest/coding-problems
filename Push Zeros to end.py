from sys import stdin





# def pushZerosAtEnd(arr, n) :
#     for i in range(n-1):
#         if arr[i] == 0:
#             for j in range(i+1,n):
#                 if arr[j]!=0:
#                     arr[i] ,arr[j] = arr[j],arr[i]
#                     break
#     return 


def pushZerosAtEnd(arr, n) :
    count = 0
    for i in range(n):
        if arr[i]!=0:
            arr[count]= arr[i]
            count+=1

    while count<n:
        arr[count] = 0
        count+=1
    return 






#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1