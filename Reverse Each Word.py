
from sys import stdin


def reverseEachWord(string) :
	lis = string.split()
	new_string = ""
	for i in lis:
		new_string+= i[::-1]+" "
	return new_string

	# Your code goes here





#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)