import sys

with open('./1.txt', 'r') as f:
     data = f.read()
# data = '''
# +1
# +1
# -2
# '''

INIT_NUM = 0

list = data.split()

result = INIT_NUM
for i in list:
    result += int(i)

print result
