#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(c - diff)), end='')
