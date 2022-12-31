## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1

while i<=n:
    j = 1
    k= i
    while j<=i:
        print(k,end="")
        j+=1
        k-=1
    i+=1
    print()