import re

with open('./7.txt', 'r') as f:
     data = f.readlines()

# data = '''
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
# '''.strip().split('\n')
# print data

info = {}
for line in data:
    tmp = re.match(r'^(\w*)\s\((\d*)\)\s->\s(.*)|^(\w*)\s\((\d*)\)', line)
    name = tmp.group(1) or tmp.group(4)
    weight = tmp.group(2) or tmp.group(5)
    holdings = tmp.group(3).split(', ') if tmp.group(3) else []

    info[name] = {}
    info[name]['weight'] = weight
    info[name]['holdings'] = holdings

holdings_list = []

for key in info:
    if info[key]['holdings']:
        for x in info[key]['holdings']:
            holdings_list.append(x)

print info.keys()
print holdings_list
for x in info.keys():
    if x not in holdings_list:
        print x
