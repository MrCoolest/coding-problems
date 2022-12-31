# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *


## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
space = n//2+1
i = 1


while (i<=space):
    # print(" "*(i-1),'* '*i)
    s = 1
    while (s<i):
        print(' ',end='')
        s+=1
    j = 1
    while(j<=i):
        print("* ",end='')
        j+=1
    i+=1
    print()

i = (space-1)
while (i>=1):
    # print(" "*(i-1),'* '*i)
    s = 1
    while (s<i):
        print(' ',end='')
        s+=1
    j = 1
    while(j<=i):
        print("* ",end='')
        j+=1
    i-=1
    print()