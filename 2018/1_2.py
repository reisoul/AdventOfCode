import sys

with open('./1.txt', 'r') as f:
     data = f.read()
# data = '''
# +7 +7 -2 -7 -4
# '''

INIT_NUM = 0
idx = 0
list = data.split()
result = INIT_NUM
first_list = [INIT_NUM]
data_len = len(list)
loop_cnt = 0

while True:
    num = int(list[idx])
    result += num
    if result in first_list:
        break
    first_list.append(result)
    # if idx==0:
        # print first_list
    idx = (idx + 1) % data_len
    loop_cnt += 1
    if (loop_cnt % 10000) == 0:
        print loop_cnt
        print result

# print first_list
print result

# very very slow.....
