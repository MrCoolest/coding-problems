#Write Your Code Here
# Reverse number
n = int(input())
reverse = 0
while n!=0:
    rem = n%10
    reverse= reverse*10+rem
    n//=10
    
print(reverse)
    