import sys

with open('./2.txt', 'r') as f:
     data = f.read()
# data = '''
# abcdef
# bababc
# abbcde
# abcccd
# aabcdd
# abcdee
# ababab
# '''

data_list = data.split()
twice = 0
three_times = 0

for data in data_list:
    char_list = set(data)
    all_list = list(data)
    twice_flag = False
    three_times_flag = False

    for char in char_list:
        cnt = all_list.count(char)
        if cnt == 2:
            twice_flag = True
        if cnt == 3:
            three_times_flag = True

    if twice_flag:
        twice += 1
    if three_times_flag:
        three_times += 1

print twice * three_times
