# Read input as sepcified in the question
# Print output as specified in the question
s = int(input())
e = int(input())
w = int(input())

c = s 
while(c<=e):
    print(str(c)+" "+str(int((c-32)*5/9)))
    c+=w
