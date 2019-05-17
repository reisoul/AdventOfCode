import sys

with open('./4.txt', 'r') as f:
     data = f.read()

lines = filter(None, data.split('\n'))

valid_count = 0
for line in lines:
    words = line.split()
    if len(words) == len(set(words)):
        valid_count += 1

print valid_count
# print words
