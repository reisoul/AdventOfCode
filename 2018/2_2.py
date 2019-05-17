import sys

with open('./2.txt', 'r') as f:
     data = f.read()
# data = '''
# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# '''

data_list = data.split()
char_len = len(data_list[0]) #sampling

for idx in range(len(data_list)-1):
    char_list = list(data_list[idx])

    for target_idx in range(idx+1, len(data_list)):
        target_char_list = list(data_list[target_idx])
        diff_cnt = 0

        for diff_idx in range(char_len):
            if char_list[diff_idx] != target_char_list[diff_idx]:
                diff_cnt += 1

            if diff_cnt > 1:
                continue

        if diff_cnt <= 1:
            print char_list
            print target_char_list
            result_list = [x for x in char_list if x in target_char_list]
            print result_list
            print ''.join(result_list)
            break
