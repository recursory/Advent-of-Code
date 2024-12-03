import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("no valid input file provided via command line")

valid_count = 0

for line in f:
    nums = line.split()
    increasing = bool(int(nums[1]) - int(nums[0]) > 0)
    valid = True
    for i in range(0, len(nums)-1):
        diff = int(nums[i+1]) - int(nums[i])#second minus first so positive means increasing
        if diff == 0 or abs(diff) > 3 or (diff > 0) != increasing:
            valid = False
            break
    if valid:
        valid_count += 1

print(valid_count)