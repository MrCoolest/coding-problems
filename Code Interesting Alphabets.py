
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
    j=1
    first_char = chr(ord('A')+n-i) 
    while j<=i:
        print(chr(ord(first_char)+j-1),end="")
        j+=1
    i+=1
    print()
