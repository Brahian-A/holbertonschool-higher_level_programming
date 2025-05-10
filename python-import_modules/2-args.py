#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_len = len(sys.argv) - 1

    if args_len == 1:
        print("{} argument:".format(args_len))
    elif args_len == 0:
        print("{} arguments.".format(args_len))
    else:
        print("{} arguments:".format(args_len))

    idx = 1
    for arg in sys.argv[1:]:
        print("{}: {}". format(idx, arg))
        idx += 1
