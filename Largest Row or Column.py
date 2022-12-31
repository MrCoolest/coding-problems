'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    # print(arr,nRows,mCols)

    row_sum = -2147483648
    row_index = 0
    for row in range(len(arr)):
        sums = sum(arr[row])
        if sums>row_sum:
            row_sum = sums
            row_index = row

    column_sum = -2147483648
    column_index = 0
    for col in range(mCols):
        sums = 0
        for j in range(nRows):
            sums+=arr[j][col]
        
        if sums>column_sum:
            column_index = col
            column_sum = sums 
    
    if row_sum>=column_sum:
        print('row'+" "+str(row_index)+" "+str(row_sum))
    else:
        print('column'+" "+str(column_index)+" "+str(column_sum))



    #Your code goes here




#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1