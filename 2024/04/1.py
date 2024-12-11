import sys
import re

xmas = 'XMAS'
count = 0

def findum(x, y, xdir, ydir, arr, search):
    if len(search) < 1:
        return 1
    if xdir == 0 and ydir == 0 or x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr):
        return 0
    if arr[y][x] == search[0]:
        return findum(x + xdir, y + ydir, xdir, ydir, arr, search[1:])
    return 0

f = open(sys.argv[1], 'rt')

arr = []
count = 0

for line in f:
    arr.append(line[:len(line)-1])
for y in range(0, len(arr)):
    for x in range(0, len(arr[0])):
        for ydir in range(-1, 2):
            for xdir in range(-1, 2):
                count += findum(x, y, xdir, ydir, arr, xmas)
print(count)
