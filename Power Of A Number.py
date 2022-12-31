## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
a, b = input().split()
a = int(a)
b = int(b)

# Normal way
# print(a**b)

# Through Recursion
def PowerOfN(a,b):
    if b==1:
        return a
    elif b == 0:
        return 1
    return a*PowerOfN(a,b-1) 

print(PowerOfN(a,b))