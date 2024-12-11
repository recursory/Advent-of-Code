import sys
f = open(sys.argv[1], 'rt')
adj = {}
goodmidsum = 0
for line in f:
    if '|' in line:
        key = int(line.partition('|')[0])
        val = int(line.partition('|')[2])
        if key not in adj:
            adj[key] = []
        adj[key].append(val)
        print(adj[key])
    elif line == '\n':
        continue
    else:
        print(line)
        words = line.partition(',')
        nums = []
        for word in words:
            nums.append(int(word.strip()))
        good = True
        for num in nums:
            blines = []
            blines.append(int(num))
            if int(num) in adj:
                for preq in  adj[int(num)]:
                    if preq not in blines:
                        good = False
                        print('epic fail!')
        if good:
            print('epic win!')
            goodmidsum += int(nums[len(nums)/2])

print(adj)
