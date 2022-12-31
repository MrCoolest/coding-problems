## Read input as specified in the question.
## Print output as specified in the question.

def reverse(string):
    if len(string)== 0:
        return string
    
    assum = reverse(string[1:])
    return assum + string[0]



# Checking Palindrome reverse string and original string are same
string = input()
if reverse(string) == string:
    print('true')
else:
    print('false')
