## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1

while i<=n:
    print(" "*(n-i),end="")
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    i+=1
    print() 