
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = n

while n>0:
    j=1
    while j<=n:
        print(j,end='')
        j+=1
    n-=1
    print() 