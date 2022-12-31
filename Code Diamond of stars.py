
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
k = (n//2+1)
while i<=k:
    if i <=k:
        print(' '*(k-i),end='')
        j = 1
        while j<=(i+(i-1)):
            print('*',end='')
            j+=1
    else:
        print(' '*(i-k),end='')
        j = 1

    i+=1
    print()

i=k-1
while i>=1:
    print(' '*(k-i),end='')
    j = 1
    while j<=(i+(i-1)):
        print('*',end='')
        j+=1
    i-=1
    print()

