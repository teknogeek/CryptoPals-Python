#!/usr/bin/env python3

from binascii import hexlify, unhexlify
from sys import argv

def main():
    if len(argv) == 3:
        hexData1, hexData2 = map(unhexlify, argv[1:])
        
        xorData = ''.join(chr(c ^ c1) for c, c1 in zip(hexData1, hexData2)).encode('utf-8')
        xorHex = hexlify(xorData).decode('utf-8')

        print(xorHex)
    else:
        print('Usage: python fixed_xor.py [hex string 1] [hex string 2]')

if __name__ == '__main__':
    main()
