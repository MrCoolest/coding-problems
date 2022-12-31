# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string) == 0 or len(string) == 1:
        return string
    assum = removeConsecutiveDuplicates(string[1:])
    if string[0] == assum[0]:
        return assum
    else:
        return string[0] + assum


# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
