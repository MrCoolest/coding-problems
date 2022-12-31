
# def checkMember(n):
#     a = 0
#     b = 1
#     for i in range(0,n+1):
#         if a==n:
#             return True
#         c = a+b
#         a = b
#         b = c
#     return False


def checkMember(n):
    a = 0
    b = 1
    while a<=n:
        if a == n:
            return True
        else:
            c = a+b
            a = b
            b = c
    else:
        return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

