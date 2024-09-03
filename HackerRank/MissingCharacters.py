#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Write your code here
    missing_digits = set(str(i) for i in range(10))
    missing_chars = set(chr(i) for i in range(ord('a'), ord('z') + 1))


    for char in s:
      
        if char.isdigit():
            missing_digits.remove(char)
        elif char.isalpha():
            missing_chars.remove(char)

  
    result = ''.join(sorted(missing_digits)) + ''.join(sorted(missing_chars))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
