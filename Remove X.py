# Problem: Remove x from string
def removeX(string): 
    if len(string) == 0:
        return string
    assum = removeX(string[1:])
    if string[0] == 'x':
        return assum
    else:
        return string[0]+assum

# Main
string = input()
print(removeX(string))
