import sys
f = open(sys.argv[1], 'rt')

def printarr(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], sep='', end='')
    print()

m = [] # my map of the situation
guard = ('^', '>', 'v', '<')
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
x = 0
y = 0
found = False
for line in f:
    l = []
    for c in line:
        l.append(c)
    m.append(l)
    for i in range(0, len(guard)):
        if guard[i] in line:
            x = line.index(guard[i])
            found = True
    if not found:
        y += 1

#print(m[y][x]) # this is where the guard lives
os = (-1, 0) # offset/delta for the space the guard is currently facing

escaped = False
while not escaped:
    if m[y+os[0]][x+os[1]] != '#':
        m[y+os[0]][x+os[1]] = m[y][x]
        m[y][x] = 'X'
        y = y+os[0]
        x = x+os[1]
    else:
        d = (guard.index(m[y][x]) + 1) % 4
        m[y][x] = guard[d]
        os = dirs[d]
    if y+os[0] < 0 or y+os[0] > len(m)-1 or x+os[1] < 0 or x+os[1] > len(m[0])-1:
        m[y][x] = 'X'
        escaped = True

#printarr(m)
exes = 0
for line in m:
    exes += line.count('X')
print(exes)
