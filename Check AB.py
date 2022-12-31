
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def check_AB(val):
    if len(val) == 2:
        if val[0:2]=='bb' or 'aa':
            return True
        else:
            return False
    if len(val) ==1:
        if val[0] == 'a':
            return True
        else:
            return False
    if val[0] == 'a':
        assum = check_AB(val[1:])
        if assum:
            return True
        else:
            return False
    elif val[0:2] == 'bb':
        assum = check_AB(val[2:])
        if assum:
            return True
        else:
            return False
    else:
        return False

val = input()

if len(val)==2:
    if val != 'aa':
        print('false')
else:
    if check_AB(val):
        print('true')
    else:
        print('false')
