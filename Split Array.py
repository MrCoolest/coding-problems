
def spslit(arr,s,n,k):
    if s == len(arr):
        return n==k

    if arr[s] % 5==0:
        n+=arr[s]
    elif arr[s]%3==0 :
        k+=arr[s]
    else:
        return spslit(arr, s+1, n+arr[s], k) or spslit(arr, s+1, n, k+arr[s])
    return spslit(arr, s+1, n, k)



n = input()
arr = [int(ele) for ele in input().split()]
ans = spslit(arr, 0, 0,0)
if ans is True:
    print('true')
else:
    print('false')
