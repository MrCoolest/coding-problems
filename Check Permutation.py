
from sys import stdin


# def isPermutation(string1, string2) :
#     flag = False
#     if len(string1) == len(string2):
#         flag = True
#         for i in range(len(string1)):
#             if string1[i] not in string2 and string2[i] not in string1:
#                 flag = False
#                 break
#     return flag
# 	#Your code goes here

def isPermutation(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
 
    # If length of both strings is not same,
    # then they cannot be Permutation
    if (n1 != n2):
        return False
 
    # Sort both strings
    a = sorted(string1)
    str1 = " ".join(a)
    b = sorted(string2)
    str2 = " ".join(b)
 
    # Compare sorted strings
    # for i in range(0, n1, 1):
    # print(str1)
    # print(str2)
    if (str1 != str2):
        return False
 
    return True



	


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

