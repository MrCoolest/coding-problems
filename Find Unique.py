def count(arr,ele):
    c = 0
    for i in arr:
        if ele == i:
            c+=1
    return c

def findUnique(arr, n):
    for i in arr:
        c =count(arr,i)
        if  c == 1:
            return i


    #Your code goes here


t = input()

uniqe = []
for i in range(int(t)):
    find = int(input())
    li = [int(x) for x in input().split()]
    uniqe.append(findUnique(li,find))

for j in uniqe:
    print(j)