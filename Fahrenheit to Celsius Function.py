
import math

def printTable(start,end,step):
	for i in range(start,end+1,step):
		print(str(i)+" "+str(int((i-32)*5/9)))

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





