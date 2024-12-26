import sys
import copy
f = open(sys.argv[1], 'rt')

def printarr(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], sep='', end='\n')
    print()

m = [] # my map of the situation
zeroes = []
guard = ('^', '>', 'v', '<')
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
x = 0
y = 0
found = False
for line in f:
    l = []
    zeroes_l= []
    for c in line:
        l.append(c)
        zeroes_l.append(0)
    m.append(l)
    zeroes.append(zeroes_l)
    for i in range(0, len(guard)):
        if guard[i] in line:
            x = line.index(guard[i])
            found = True
    if not found:
        y += 1

print(len(zeroes), len(zeroes[0]))
print(len(m), len(m[0]))
loops = 0
breaktest = False
#print(m[y][x]) # this is where the guard lives
for obs_y in range(0, len(m)):
    for obs_x in range(0, len(m[obs_y])):
        print(obs_y, obs_x)
        if obs_y == y and obs_x == x:
            continue
        oy = y # guard y in the obstacle timeline
        ox = x # guard x in the obstacle timeline
        om = copy.deepcopy(m) # situation map in the obstacle timeline
        om[6][3] = 'O' # our new obstacle that we're seeing if it causes the guard to move in a loop
        trace = copy.deepcopy(zeroes) # situation map but time stamp of when guard was last there
        os = (-1, 0) # offset/delta for the space the guard is currently facing
        escaped = False
        time = 0
        last_trace_diff = 0
        same_trace_diff_count = 0
        while not escaped:
            time += 1
            print('obstacle x y =', obs_x, obs_y, ', t =', time, ', guard x y =', ox, oy, 'loops =', loops)
            printarr(om)
            printarr(trace)
            this_trace_diff = time - trace[oy][ox]
            print(time, ' -', trace[oy][ox], ' =', this_trace_diff, ' vs', last_trace_diff, ' #', same_trace_diff_count)
            if time > 100:
                assert False
            if last_trace_diff == this_trace_diff:
                same_trace_diff_count += 1
            else:
                same_trace_diff_count = 0
            if same_trace_diff_count > 10:
                loops += 1
                print('break test')
                breaktest = True
            trace[oy][ox] = time
            last_trace_diff = this_trace_diff
            if om[oy+os[0]][ox+os[1]] == '.':
                om[oy+os[0]][ox+os[1]] = om[oy][ox]
                om[oy][ox] = '.'
                oy = oy+os[0]
                ox = ox+os[1]
            else:
                d = (guard.index(om[oy][ox]) + 1) % 4
                om[oy][ox] = guard[d]
                os = dirs[d]
            if oy+os[0] < 0 or oy+os[0] > len(om)-1 or ox+os[1] < 0 or ox+os[1] > len(om[0])-1:
                print('escape!')
                escaped = True
        if breaktest:
            print('break test success!')
            breaktest = False

#printarr(m)
print(loops)
