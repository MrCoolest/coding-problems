## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
# while i<=n:
#     print(' '*(n-i),'*'*(i+(i-1)))
#     i+=1

while i<=n:
    print(' '*(n-i),end='')
    j = (i+(i-1))
    while j>=1:
        print('*',end='')
        j-=1
    i+=1
    print()