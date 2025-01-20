#!/usr/bin/python3
for abc in range(97, 123):
    if chr(abc) not in ['q', 'e']:
        print("{}".format(chr(abc)), end="")
