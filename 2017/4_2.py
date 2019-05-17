import itertools

with open('./4.txt', 'r') as f:
     data = f.read()

lines = filter(None, data.split('\n'))

valid_count = 0
# break_num = 0

for line in lines:
    words = filter(None, line.split())
    word_set = []

    for word in words:
        word_dict = {}
        ch_list = [x for x in word]
        ch_set = set(ch_list)
        for ch in ch_set:
            word_dict[ch] = len(filter(lambda x: x == ch, ch_list))
        word_set.append(word_dict)

    # print words, len(words)
    # print [x[0] for x  in itertools.groupby(word_set)], len([x[0] for x  in itertools.groupby(word_set)])
    word_set = [x[0] for x in itertools.groupby(word_set)]
    filtered_set = []
    map(lambda x: filtered_set.append(x) if x not in filtered_set else None, word_set)

    if len(words) != len(word_set):
        continue

    if len(words) != len(filtered_set):
        continue

    valid_count += 1
    # print str(word_set)
    # print str(filtered_set)

    # break_num += 1
    # if break_num == 2:
    #     break

print valid_count
