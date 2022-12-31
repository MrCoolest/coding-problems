## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n = int(input())
odd = 0
even = 0

while n!=0:
    last_dig = n%10
    if(last_dig%2==0):
        even+=last_dig
    else:
        odd+=last_dig
    n//=10

print(even, " ", odd)