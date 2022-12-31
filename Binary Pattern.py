
## Read input as specified in the question.
## Print output as specified in the question.

n =int(input())

for i in range(1,n+1):
    if i%2==0:
        print('0'*(n-i+1))
    else:
        print('1'*(n-i+1))