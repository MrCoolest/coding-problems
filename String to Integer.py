# Write your code here...

def str_to_int(string):
    if string=="":
        return 0
    assum = str_to_int(string[1:]) * 10 + ord(string[0])-48
    return assum



string = str(int(input()))[::-1]

print(str_to_int(string))