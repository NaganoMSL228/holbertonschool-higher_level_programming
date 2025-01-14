#!/usr/bin/python3
for i in range(26):
    char = chr(122 - i) if i % 2 == 0 else chr(90 - i)  # 122 is 'z', 90 is 'Y'
    print(char, end='')
