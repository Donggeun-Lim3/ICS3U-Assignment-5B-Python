#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program is nested loop

def main():
    counter1 = 0
    counter2 = 0

    for counter1 in range(10):
        for counter2 in range(10):
            result = counter1 * counter2
            print("{0} x {1} = {2}".format(counter1, counter2, result))


if __name__ == "__main__":
    main()
