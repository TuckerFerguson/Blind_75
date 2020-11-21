# Author: Tucker Ferguson
# Date: 10/26/2020
#
# Description: Reverse bits of a given 32 bits unsigned integer
#
# Link: https://leetcode.com/problems/reverse-bits/
import sys
def reverseBit(n):
    lastIndex = 0
    for i in range(len(bin(n))):
        if bin(n)[i] == '1':
            lastIndex = i
    return int(bin(n)[2:].zfill(32)[::-1],2)        

    
print(reverseBit(43261596))