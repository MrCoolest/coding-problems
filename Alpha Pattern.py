## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
    print(chr(ord('A')+i-1)*i)
    i+=1