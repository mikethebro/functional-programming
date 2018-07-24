#!/bin/python
import os
import sys

def sockMerchant(n, ar):
    colors = {}
    for a in ar:
        if a in colors:
            colors[a] = colors[a] + 1
        else:
            colors[a] = 1
    total_pairs = 0
    for color in colors:
        pairs = colors[color] / 2
        total_pairs += pairs
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
