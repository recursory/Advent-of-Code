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
        #print(adj)
        continue
    else:
        #print()
        words = line.strip().split(',')
        nums = []
        for word in words:
            nums.append(int(word))
        good = True
        sofars = []
        for num in nums:
            sofars.append(num)
            if num in adj:
                for preq in adj[num]:
                    if preq in nums and preq not in sofars:
                        #print("epic fail!")
                        #print(adj[num])
                        #print(sofars)
                        good = False
        if good:
            #print("epic win!")
            goodmidsum += nums[int(len(nums)/2)]
print(goodmidsum)
