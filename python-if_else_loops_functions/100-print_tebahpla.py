#!/usr/bin/python3
check = 1
for i in range(122, 96, -1):
    if check == 0:
        print("{}".format(chr(i - 32)), end="")
        check = 1
    elif check == 1:
        print("{}".format(chr(i)), end="")
        check = 0
