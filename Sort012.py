from sys import stdin 

# def sort012(arr, n) :
#     for i in range(1,n):
#         for j in range(i-1,-1,-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
    #Your code goes here


def sort012(arr, n):
    zero = 0
    one = 0
    two = 0
    for i in range(n):
        if arr[i]==0:
            zero+=1
        elif arr[i] == 1:
            one+=1
        else:
            two+=1
    
    if zero or one or two:
        arr[0:n] = [0]*zero+[1]*one+[2]*two
    return arr







#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1
