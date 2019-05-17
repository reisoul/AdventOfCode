with open('./5.txt', 'r') as f:
  data = map(lambda x: int(x), filter(None, f.read().split('\n')))

# data = [0, 3, 0, 1, -3]
max_idx = len(data) - 1
step_cnt = 0
start_idx = 0

while True:
    offset = data[start_idx]
    if offset < 3:
      data[start_idx] += 1
    else:
      data[start_idx] -= 1
    start_idx += offset

    step_cnt += 1
    # print str(data), step_cnt
    if start_idx > max_idx:
      break

print step_cnt
