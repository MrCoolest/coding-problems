def checkPalindrome(num):
#Implement Your Code Here
	num_copy = num
	reverse = 0
	while num>0:
		rem = num%10
		reverse = reverse*10+rem
		num//=10
	return num_copy == reverse
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
