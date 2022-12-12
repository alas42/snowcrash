#!/usr/bin/python3
import sys
import math
import base64
import codecs
import binascii

#It basically decode what the level09 output encodes
#reversing its rules: every character at index n has to have n removed from its ascii code
#After 126 it is non printable, so we % it to 127 to pass it from 0 to 126
#Not forgetting to strip the string from newlines
def main():
    with open("token", 'rb') as f:
        token = f.read()
    token = token.strip()
    good_token = ""
    i = 0
    for ch in token:
        char = chr((ch - i) % 127)
        good_token = ''.join((good_token, char))
        i = i + 1
    print(good_token)

main()