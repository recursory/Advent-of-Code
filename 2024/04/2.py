import sys
f = open(sys.argv[1], 'rt')

arr = []
count = 0

for line in f:
    arr.append(line[:len(line)-1])
for y in range(1, len(arr)-1):
    for x in range(1, len(arr[0])-1):
        if arr[y][x] == 'A':
            if arr[y-1][x-1] == 'M' and arr[y+1][x+1] == 'S' or arr[y-1][x-1] == 'S' and arr[y+1][x+1] == 'M':
                if arr[y-1][x+1] == 'M' and arr[y+1][x-1] == 'S' or arr[y-1][x+1] == 'S' and arr[y+1][x-1] == 'M':
                    count += 1
print(count)
