def checkPalindrome(num):
	og = num
	rev = 0
	while num!=0:
		rem = num%10
		rev = rev * 10 + rem
		num//=10
	return og == rev  
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
