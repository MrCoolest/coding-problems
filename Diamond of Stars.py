#   *
#  ***
# *****
#  ***
#   *


## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

c = (n//2)

for i in range(1, n+1, 2):
    # space
    # print(c-i+1)
    for j in range(0, c):
        print(" ", end="")

    c -= 1
    # stars
    for k in range(1, i+1):
        print("*", end="")
    print()

for i in range(n-2, 0, -2):
    # space
    # print(c-i+1)
    c += 1
    for j in range(0, c+1):
        print(" ", end="")

    # stars
    for k in range(1, i+1):
        print("*", end="")
    print()
