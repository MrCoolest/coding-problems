from sys import stdin

# Need TO Practice This


# def spiralPrint(mat, nRows, mCols):
#     # print(mat, nRows, mCols)
#     ans = []
#     if nRows == 0:
#         print()
    
#     seen = [[0 for i in range(mCols)] for j in range(nRows)]
#     dr = [0,1,0,-1]
#     dc = [1,0,-1,0]
#     x = 0
#     y = 0
#     di= 0
#     for i in range(nRows*mCols):
#         print(mat[x][y],end=" ")
#         seen[x][y] = True
#         cr = x+dr[di]
#         cc = y+dc[di]
#         if (0<=cr and cr<nRows and 0<=cc and cc<mCols and not(seen[cr][cc])):
#             x = cr
#             y = cc
#         else:
#             di = (di+1)%4
#             x+=dr[di]
#             y+=dc[di]


# def spiralPrint(mat, nRows, mCols):
#     # print(mat, nRows, mCols)
#     # ans = []
#     if nRows == 0:
#         print()
    
#     row_start = 0
#     row_end = nRows-1
#     column_start = 0
#     column_end = mCols-1
#     while(row_start<=row_end and column_start <=column_end):
#         for i in range(column_start,column_end+1):
#             print(mat[row_start][i],end=" ")
        
#         row_start+=1
#         for j in range(row_start,row_end+1):
#             print(mat[j][column_end],end=" ")
        
#         column_end-=1

#         for k in range(column_end, column_start-1,-1):
#             print(mat[row_end][k],end=" ")
#         row_end-=1

#         for o in range(row_end,row_start-1,-1):
#             print(mat[o][column_start],end=" ")
#         column_start+=1


def spiralPrint(a,m,n):
    
    if n == 0:
        print()
    # m = n
    # n = m
    k = 0
    l = 0

    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
              
        k += 1
  
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
              
        n -= 1
  
        if ( k < m) : 
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
              
            m -= 1
          
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1






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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
