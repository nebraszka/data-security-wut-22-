# An example of a program that performs frequency analysis of individual letters:

import sys, re
stat = {}
for line in sys.stdin.readlines():
        # re.sub(pattern, repl, string, count=0, flags=0); r\s - whitespace chars
        line = re.sub(r'\s', '', line)
        for znak in line:
                if znak in stat:
                        stat[znak] += 1
                else:
                        stat[znak] = 1

for znak in stat:
        print("{} <=> {}".format(znak, stat[znak]))