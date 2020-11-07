#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'somaDeGauss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER numeroMaximo as parameter.
#

def somaDeGauss(numeroMaximo):
    x = 1
    result = 0
    while x <= numeroMaximo:
        x = x + 1
        result = x + result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numeroMaximo = int(input().strip())

    result = somaDeGauss(numeroMaximo)

    fptr.write(str(result) + '\n')

    fptr.close()
