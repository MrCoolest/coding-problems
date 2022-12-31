from sys import stdin


# def intersection(arr1, arr2, n, m) :
# 	#Your code goes here
#     if n <m:
#         arr2.sort()
#         for i in arr2:
#             if i in arr1:
#                 print(i,end=" ")
#                 arr1.remove(i)
#     else:
#         arr1.sort()
#         for i in arr1:
#             if i in arr2:
#                 print(i,end=" ")
#                 arr2.remove(i)


def intersection(arr1, arr2, n, m) :
	#Your code goes here
    arr2.sort()
    arr1.sort()

    if n <m:
       merge(arr1,n,arr2,m)
    else:
       merge(arr2,m,arr1,n)


def merge(arr1, n, arr2, m):
    i = 0
    j = 0
    # print(arr1,arr2,n,m)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i],end=' ')
            i+=1
            j+=1





























# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1
