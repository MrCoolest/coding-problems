
from sys import stdin


# def pairSum(arr, n, x) :
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]>arr[j]:
#                 min_ele = arr[j]
#                 max_ele = arr[i]
#             else:
#                 min_ele = arr[i]
#                 max_ele = arr[j]
#             # min_ele = min(arr[i],arr[j])
#             # max_ele = max(arr[i],arr[j]) 
#             lis = [min_ele,max_ele]
#             pair_total = sum(lis)
#             if pair_total==x:
#                 count+=1
    
                    
#     return count


def pairSum(arr, n, x) :
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                min_ele = arr[j]
                max_ele = arr[i]
            else:
                min_ele = arr[i]
                max_ele = arr[j]
            if min_ele+max_ele==x:
                count+=1
    
                    
    return count

    #Your code goes here

# def pairSum(arr, n, x) :
#     count=0
#     for i in range(n):
#         cur  = arr[i]
#         want = x-cur
#         if want in arr[i+1:]:
#             count+=1
#     return count




#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1