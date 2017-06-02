#!/usr/bin/env python3
from binascii import unhexlify
from string import ascii_lowercase
from single_byte_xor import calcIC, ENGLISH_IC

def main():
    # read the lines from the challenge file into a list
    hexList = open('4.txt').read().splitlines()

    bestDiff = 9999
    res = ''

    # decode all the hex strings
    hexDataList = list(map(unhexlify, hexList))
    for hexData in hexDataList:
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

if __name__ == '__main__':
    main()
