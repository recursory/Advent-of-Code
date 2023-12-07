import sys

try:
    f = open(sys.argv[1], "rt")
except:
    print("error: failure to open input file specified on command line")

t = 0
for line in f:
    #print(line)
    for cha in line:
        #print(f'is {cha} alphanumeric?')
        if cha.isnumeric():
            #print('yes')
            fir = cha
            break
    for cha in reversed(line):
        #print(f'is {cha} alphanumeric?')
        if cha.isnumeric():
            #print('yes')
            sec = cha
            break
    #print(f'{fir} + {sec} = {10*int(fir)+int(sec)}')
    t = t + 10 * int(fir) + int(sec)
print(t)
