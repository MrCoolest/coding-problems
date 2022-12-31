def mergeSort(arr, start, end):
    if len(arr) ==0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1, start, mid+1)
    mergeSort(a2, mid+1, end)
    # print(s1,s2)
    mergeTwoList(a1,a2,arr)



def mergeTwoList(lis1,lis2,arr):
    l1 = 0
    l2 = 0
    k = 0
    # print(lis1)
    # print(lis2)
    while l1<len(lis1) and l2<len(lis2):
        if lis1[l1] <= lis2[l2]:
            arr[k] = lis1[l1]
            k+=1
            l1+=1
        else:
            arr[k] = lis2[l2]
            l2+=1
            k+=1
    
    if l1<len(lis1):
        arr[k:] = lis1[l1:]
    if l2<len(lis2):
        arr[k:] = lis2[l2:]   



# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
