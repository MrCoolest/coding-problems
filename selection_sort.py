from sys import stdin

def selectionSort(arr, n) :
    for i in range(n):
        min_val = i
        for j in range(i+1,n):
            if arr[min_val]>arr[j]:
                min_val = j
        # print(min_val)
        if i != min_val:
            arr[i], arr[min_val] = arr[min_val], arr[i]
    return
            
    #Your code goes here


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
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
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1