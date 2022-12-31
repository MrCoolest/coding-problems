## Read input as specified in the question.
## Print output as specified in the question.

s = input()

s_lis = s.split()

min_len = len(s)
min_word = ""

for i in s_lis:
    if min_len > len(i):
        min_word = i
        min_len = len(i)

print(min_word)
