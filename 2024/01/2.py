import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("error: failure to open input file specified on command line")

left = []
rightct = {}

for line in f:
    leftnum = int(line.split()[0])
    rightnum = int(line.split()[1])
    left.append(leftnum)
    if rightnum in rightct:
        rightct[rightnum] += 1
    else:
        rightct[rightnum] = 1

similarity = 0

for leftnum in left:
    if leftnum in rightct:
        similarity += leftnum * rightct[leftnum]

print(similarity)
