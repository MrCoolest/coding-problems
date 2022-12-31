from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)



def getCompressedString(input) :
	# pass
	new_string = input[0]
	count=0
	for i in input:
		if new_string[-1] == i:
			count+=1
		else:
			if count >1:
				new_string+=str(count)
			new_string+=i
			count=1
	if count>1:
		new_string+=str(count)
	return new_string


# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)