import copy


data_str = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'
# data_str = '4    1    15    12    0    9    9    5    5    8    7    3    14    5    12    3'
# data_str = '0 2 7 0'
data = map(lambda x: int(x), data_str.split())
dist_cnt = len(data)
snapshot_list = [copy.deepcopy(data)]
# cnt = 0

while True:
    select_value = max(data)
    select_idx = data.index(select_value)

    data[select_idx] = 0
    for offset in xrange(1, select_value+1):
        data[(select_idx+offset)%dist_cnt] += 1

    if data in snapshot_list:
        break

    snapshot_list.append(copy.deepcopy(data))
    # cnt+=1
    #
    # if cnt==10:
        # break

# import pprint
# pprint.pprint(snapshot_list)
print len(snapshot_list), snapshot_list.index(data)
print len(snapshot_list)-snapshot_list.index(data) # star2
# print "result: " + str(len(snapshot_list)) # star1
print str(data)
