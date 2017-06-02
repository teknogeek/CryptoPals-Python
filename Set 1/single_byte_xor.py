#!/usr/bin/env python3

from binascii import unhexlify
from string import ascii_uppercase
from sys import argv

# Index of Coincidence for English
ENGLISH_IC = 1.73


def calcIC(s: str) -> int:
    '''Calculates the Index of Coincidence for a string'''

    # remove spaces from the string before calculating the IC
    s = s.replace(' ', '').upper()
    sLen = len(s)

    ic = 0
    for c in ascii_uppercase:
        # frequency of the letter, c, in s
        freq = s.count(c)
        ic += freq * (freq - 1)
    
    ic /= (sLen * (sLen - 1)) / 26

    return ic

def main():
    if len(argv) == 2:
        # decode hex string
        hexData = unhexlify(argv[1])
        
        bestDiff = 9999
        res = ''

        # iterate over bytes from 0x00 - 0x7F
        for x in range(127):
            # XOR the strin
            decStr = ''.join(chr(x ^ c) for c in hexData)

            # calculate the IC for the current string
            ic = calcIC(decStr)

            # find how close the IC is to the english IC
            diff = abs(ENGLISH_IC - ic)

            # if the current string is closer to the english IC, make this the best answer
            if diff < bestDiff:
                bestDiff = diff
                res = decStr

        print(res)
    else:
        print('Usage: python single_byte_xor.py [hex string]')

if __name__ == '__main__':
    main()
