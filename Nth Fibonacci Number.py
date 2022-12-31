## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = 0
b = 1
count = 1
while (n>count):
    c = a+b
    a= b
    b=c
    count+=1

print(b)



