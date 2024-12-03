import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("no valid input file provided via command line")

valid_count = 0

for line in f:
    nums = line.split()
    print(f"considering the line {nums}:")
    increasing = bool(int(nums[1]) - int(nums[0]) > 0)
    print(f"are the first two increasing? {increasing}.")
    valid = True
    print("stepping through this list,")
    for i in range(0, len(nums)-1):
        print(f"considering {nums[i]} and {nums[i+1]}:")
        diff = int(nums[i+1]) - int(nums[i]) #second minus first, so positive means increasing
        print(f"their difference is {diff},")
        if (diff == 0):
            print("whose magnitude subceeds 1, so it's not valid.")
            valid = False 
            break
        elif (abs(diff) > 3):
            print("whose magnitude exceeds 3, so it's not valid.")
            valid = False
            break
        elif ((diff > 0) != increasing):
            print(f"whose sign opposes the increase direction, so it's not valid.")
            valid = False
            break
        if valid:
            print("and that's all good!")
    if valid:
        print(f"hooray, it's valid!")
        valid_count += 1
    else:
        print(f"so the line {nums} isn't valid. too bad!")
    print("")

print(valid_count)
