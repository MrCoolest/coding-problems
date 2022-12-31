from sys import stdin

# not using power of Python
# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     i = 0
#     j = 0
#     first = 0
#     second = 0
#     while i<n or j<n:
#         if i<n:
#             first = first*10+arr1[i]
#             i+=1
#         if j < m:
#             second = second*10+arr2[j]
#             j += 1
#         print(first+second)
#     return first+second
    #Your code goes here


# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     i = 0
#     j = 0
#     first = 0
#     second = 0
#     while i<n or j<m:
#         if i<n:
#             first = first*10+arr1[i]
#             i+=1
#         if j < m:
#             second = second*10+arr2[j]
#             j += 1
#         # print(first+second)
#     # return first+second
#     final_value = str(first+second)
#     for k in range(len(output)):
#         output[k]= final_value[k]
#     return output


def sumOfTwoArrays(arr1, n, arr2, m, output):
    i = n-1
    j = m-1
    o = len(output)-1
    cary = 0
    while i>=0 or j>=0:
        # print(i)
        # print(j)
        if i>=0 and j>=0:
            sum = arr1[i]+arr2[j]+cary
            unit = (sum%10)
            cary = (sum//10)
            output[o] = unit
            j-=1
            i-=1
            o-=1
        else:
            if i >=0:
                output[o] = arr1[i]+cary
                o-=1
                i-=1
                cary = 0
            elif j>=0:
                output[o] = arr2[j]+cary
                cary =0
                o-=1
                j-=1
    if cary:
        output[o]=cary
        o-=1
    return output




















#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1
