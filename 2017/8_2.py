import re

with open('./8.txt', 'r') as f:
     data = f.read()
# data = '''
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# '''

lines = filter(None, data.split('\n'))

registers = {}
max_value = -9999

for line in lines:
    words = line.split()
    if len(words) <= 0:
        continue

    cond_sub = str(words[4])

    if cond_sub not in registers:
        registers[cond_sub] = 0
        # print cond_sub + ' #1'

    if eval(' '.join(["registers['"+words[4]+"']"] + words[5:])):
        cond_sub = str(words[0])
        if cond_sub not in registers:
            registers[cond_sub] = 0
            # print cond_sub + ' #2'

        if words[1] == 'inc':
            registers[cond_sub] += int(words[2])
        elif words[1] == 'dec':
            registers[cond_sub] -= int(words[2])

        if registers[cond_sub] >= max_value:
            max_value = registers[cond_sub]

key, value = max(registers.iteritems(), key=lambda x:x[1])
print registers
print value
print max_value
