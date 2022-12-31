## Read input as specified in the question
## Print the required output in given format
n = int(input())
i=1

while(i<=n):
    j = 1
    start_char = ord('A')+i-1
    while(j<=i):
        ch = chr(start_char+j-1)
        print(ch,end="")
        j+=1
    i+=1
    print()