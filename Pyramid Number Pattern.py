#    1
#   212
#  32123
# 4321234
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1

while(i<=n):
    j=i
    print(' '*(n-i),end='')
    while(j>=1):
        print(j,end='')
        j-=1
    j+=2
    while(j<=i):
        print(j,end='')
        j+=1
    i+=1
    print()