import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("error: failure to open input file specified on command line")

numbers = [
        ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
]

t = 0
for line in f:
    line = line.replace('\n', '')
    rline = line[::-1]
    for i in range(0, len(line)-3): 
        for numlen in range(3, 6):
            if len(line) - i + 1> numlen:
                for j in range(0, 10):
                    if numbers[0][j] in line[i:i+numlen]:
                        line = line.replace(numbers[0][j], numbers[1][j], 1)
    for i in range(0, len(rline)-3): 
        for numlen in range(3, 6):
            if len(rline) - i + 1> numlen:
                for j in range(0, 10):
                    if numbers[0][j][::-1] in rline[i:i+numlen]:
                        rline = rline.replace(numbers[0][j][::-1], numbers[1][j], 1)

    for cha in line:
        if cha.isnumeric():
            fir = cha
            break
    for cha in rline:
        if cha.isnumeric():
            sec = cha
            break
    t = t + 10 * int(fir) + int(sec)
print(t)
