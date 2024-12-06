import sys
import re

try:
    f = open(sys.argv[1], "rt")
except:
    print("no valid input file provided via command line")

instr = []

for line in f:
   inst = re.findall("mul\(\d+,\d+\)", line) 
   instr.extend(inst)

s = 0

for mul in instr:
    ops = re.findall("\d+", mul)
    d = int(ops[0]) * int(ops[1])
    s += d

print(s)

