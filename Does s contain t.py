def contains(s,t):
    # print(s,t)
    if len(s) == 0:
        print('false')
        return False
    if len(t) == 0:
        print('true')
        return 1
    # print(t)
    # print(s)
    # print(s,t)
    if s[0] == t[0]:
        assum = contains(s[1:],t[1:])
        # print('2',assum)
        return assum
    else:
        assum = contains(s[1:],t)
        # print('3',assum)
        # print('assum',assum)
        return assum
    
s = input()
t = input()

ans = contains(s,t)
# if ans is True:
#     print('true')
# else:
#     print('false')