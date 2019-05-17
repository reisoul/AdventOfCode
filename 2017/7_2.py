import re
import pprint
#
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

info = {}
for line in data:
    tmp = re.match(r'^(\w*)\s\((\d*)\)\s->\s(.*)|^(\w*)\s\((\d*)\)', line)
    name = tmp.group(1) or tmp.group(4)
    weight = tmp.group(2) or tmp.group(5)
    holdings = tmp.group(3).split(', ') if tmp.group(3) else []

    info[name] = {}
    info[name]['weight'] = weight
    info[name]['holdings'] = holdings

fixed = 0
result = {}
while True:
    for key in info:
        if info[key]['holdings'] and not info[key].has_key('total_weight'):
            flag = len(info[key]['holdings'])
            for x in info[key]['holdings']:
                if info[x].has_key('total_weight') or not info[x]['holdings']:
                    flag -= 1
            if flag == 0:
                sum = 0
                values = []
                for x in info[key]['holdings']:
                    add = int(info[x]['total_weight']) if info[x].has_key('total_weight') else int(info[x]['weight'])
                    values.append(add)
                    sum += int(add)
                sum += int(info[key]['weight'])
                info[key]['total_weight'] = sum
                info[key]['balanced'] = False

                if fixed == 0 and len(set(values)) != 1:
                    result['holdings'] = info[key]['holdings']
                    result['values'] = values
                    fixed += 1

    # if info['tknk'].has_key('total_weight'):
    if info['hlqnsbe'].has_key('total_weight'):
        break

print result
# pprint.pprint(info)
