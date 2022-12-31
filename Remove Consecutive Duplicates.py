
from sys import stdin

def removeConsecutiveDuplicates(string) :
	new_string = ''
	copy = string+" "
	for i in range(len(string)):
		if copy[i] != copy[i+1]:
			new_string+=string[i]
	return new_string
	# Your code goes here


	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)