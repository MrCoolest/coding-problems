from sys import stdin


def findDuplicate(li, n) :
    sum = 0
    sum1 = 0

    for i in range(n):
        sum = sum + i

    for i in range(len(li)):
        sum1 = sum1 + li[i]
    # print(sum1,sum)
    res = sum - sum1
    return n - 1 - res
    #Your code goes here




























    



#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1
