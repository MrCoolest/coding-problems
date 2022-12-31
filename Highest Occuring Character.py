
from sys import stdin


def highestOccuringChar(string) :
	st = ""
	for i in string:
		if i not in st:
			st+=i

	count = 0
	char = string[0]
	for i in st:
		val = string.count(i)
		if val>count:
			count=val
			char = i
	return char
	
	#Your code goes here



#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)