## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i= 1

while i<=n:
    print(' '*(n-i),end="")
    j = i
    while j <= (i+(i-1)):
        print(j,end='')
        j+=1
    k=j-2
    while k >=i:
        print(k,end='')
        k-=1
    i+=1
    print()