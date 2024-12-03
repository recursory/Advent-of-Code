import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("error: failure to open input file specified on command line")

left = []
right = []

for line in f:
    nums = line.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()

result = 0

for i in range(0, len(left)):
    diff = left[i] - right[i]
    if diff < 0:
        diff = diff * -1
    result += diff
print(result)
