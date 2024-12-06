import sys
import re

try:
    f = open(sys.argv[1], "rt")
except:
    print("no valid input file provided via command line")

bulks = []

for line in f:
    bulk = re.findall("(.*?)(don\'t\(\)?)(.*?)(do\(\)?)", line)
    for bul in bulk:
        for i in range(0, len(bul)):
            if(i%4 == 0):
                bulks.append(bul[i])
    bulk = re.findall("(.*)(do\(\))(.*?)(\n)", line)
    bulks.append(bulk[0][2])

instr = []

for line in bulks:
    inst = re.findall("mul\(\d+,\d+\)", line) 
    instr.extend(inst)

s = 0

for mul in instr:
    ops = re.findall("\d+", mul)
    d = int(ops[0]) * int(ops[1])
    s += d

print(s)
