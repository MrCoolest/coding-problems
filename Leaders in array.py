## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

lis = [int(i) for i in input().split()]
# print(lis.index(max(lis)))
max_val = max(lis)
max_index = lis.index(max_val)

str_to_print = str(max_val)

rough = ""


for i in range(n):
    j = i+1
    while j<n:
        if lis[i]<lis[j]:
            break
        j+=1
    if j == n: 
        print(lis[i], end=' ')


