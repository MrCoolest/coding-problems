# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(1,n+1):
    # space
    for j in range(1,i):
        print(' ',end='')
    # increment
    for k in range(i,n+1):
        print(k,end='')
    print()

for i in range(n-1,0,-1):
    # space
    for j in range(1,i):
        print(' ',end='')
    # increment
    for k in range(i,n+1):
        print(k,end='')
    print()