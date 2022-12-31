
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	new_string = ""
	for i in string:
		if i != ch:
			new_string+=i
	return new_string
	# Your code goes here




	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)