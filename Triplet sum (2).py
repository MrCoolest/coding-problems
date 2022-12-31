from sys import stdin
import math as mt
import bisect

def tripletSum(arr, n, k) :
    arr.sort()
    numTriples = 0
    for i in range(n):
        pairSumFor = k - arr[i]
        numPairs = pairSum(arr,(i+1),(n-1),pairSumFor)
        numTriples+=numPairs
    return int(numTriples)

	#Your code goes here

def pairSum(arr,startIndex, endIndex,num):
    numPair = 0
    while (startIndex<endIndex):
        if(arr[startIndex] + arr[endIndex]<num):
            startIndex+=1
        elif(arr[startIndex] + arr[endIndex]>num):
            endIndex-=1
        else:
            elementAtStart = arr[startIndex]
            elementAtEnd = arr[endIndex]
            if(elementAtStart == elementAtEnd):
                totalElementFromStartToEnd = (endIndex-startIndex) +1
                numPair += (totalElementFromStartToEnd*(totalElementFromStartToEnd-1)/2)
                return numPair
            tempStartIndex = startIndex+1
            tempEndIndex = endIndex-1

            while(tempStartIndex<=tempEndIndex and arr[tempStartIndex]== elementAtStart):
                tempStartIndex+=1
            
            while(tempEndIndex >= tempStartIndex and arr[tempEndIndex] == elementAtEnd):
                tempEndIndex -=1
            
            totalElementFromStart = (tempStartIndex - startIndex)
            totalElementFromEnd = (endIndex - tempEndIndex)

            numPair+= (totalElementFromStart * totalElementFromEnd)
            # print((totalElementFromStart * totalElementFromEnd))
            startIndex = tempStartIndex
            endIndex = tempEndIndex
        # print(numPair)
    return numPair
        

# def tripletSum(arr, n, Sum):
#     count = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if (arr[i]+arr[j]+arr[k] == Sum):
#                     count+=1
#                     # print(count)
#     return count




















#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1