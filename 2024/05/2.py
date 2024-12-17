import sys
f = open(sys.argv[1], 'rt')
adj = {}
goodmidsum = 0
for line in f:
    if '|' in line:
        vab = line.strip().split('|')
        val = int(vab[0])
        key = int(vab[1])
        if key not in adj:
            adj[key] = []
        adj[key].append(val)
    elif line == '\n':
        ##print(adj)
        continue
    else:
        ##print()
        words = line.strip().split(',')
        nums = []
        for word in words:
            nums.append(int(word))
        #print(nums)
        swapped = False 
        sofars = []
        for num in nums:
            sofars.append(num)
            if num in adj:
                for preq in adj[num]:
                    if preq in nums and preq not in sofars:
                        nindex = nums.index(num)
                        nums[nums.index(preq)] = num
                        nums[nindex] = preq
                        middex = nums[int(len(nums)/2)]
                        goodmidsum += middex
                        swapped = True
                    if swapped == True:
                        break
            if swapped == True:
                break 
print(goodmidsum)
