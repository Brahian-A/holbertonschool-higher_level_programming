#!/usr/bin/python3
for i in range(10):
    for h in range(10):
        if (i != h and i < h) and i < 9:
            if (i == 8 and h == 9):
                print('{0}{1}'.format(i, h))
            else:
                print('{0}{1}, '.format(i, h), end='')
