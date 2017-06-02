#!/usr/bin/env python3

from binascii import unhexlify
from base64 import b64encode
from sys import argv

def main():
    if len(argv) == 2:
        # decode hex string
        hexData = unhexlify(argv[1])

        # convert to base64 string
        b64Data = b64encode(hexData).decode('utf-8')
        
        print(b64Data)
    else:
        print('Usage: python hex2base64.py [hex string]')

if __name__ == '__main__':
    main()
