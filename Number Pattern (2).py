n = int(input())
i=1

while(i<=n):
    j = 1
    while (j<=i):
        print(j,end='')
        j+=1
    space = (n-i)+(n-i)
    while space >=1:
        print(' ',end='')
        space-=1
    j = i
    while (j>=1):
        print(j,end='')
        j-=1
    i+=1
    print()