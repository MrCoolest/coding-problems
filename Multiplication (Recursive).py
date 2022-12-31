
## Read input as specified in the question.
## Print output as specified in the question.

# def multiplication(m,n):
#     if n == 0:
#         return 0
#     if n > 0:
#         if n == 1:
#             return m
#         assum = multiplication(m,n-1)
#         return m+assum
#     else:
#         if n == -1:
#             return m
#         assum = multiplication(m, n+1)
#         return m-assum


# def multiplication(m, n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return m
#     assum = multiplication(m, n-1)
#     return m+assum

def multiplication(x, y):
    # if x is less than y swap
    # the numbers
    if x < y:
        return multiplication(y, x)

    # iteratively calculate y
    # times sum of x
    elif y != 0:
        return (x + multiplication(x, y - 1))

    # if any of the two numbers is
    # zero return zero
    else:
        return 0

m = int(input())
n = int(input())

print(multiplication(m,n))
