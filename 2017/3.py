import sys

#test_input=347991

input = int(sys.argv[1])

if input == 1:
  print 1
  exit(0)

x = 2
while True:
  if (input > (2*x-3)**2) and (input <= (2*x-1)**2):
    break

  x += 1

print "x is " + str(x)

length = 8*(x-1)
flag = 0 # 0 is down, 1 is top
max = 2*(x-1)
min = x-1
distance = max
start_num = (2*x-3)**2

for i in range(length, 0, -1):
  if (start_num+i) == input:
    print str(start_num+i) + ' ' + str(distance)

  if flag == 0:
    distance -= 1
  else:
    distance += 1

  if distance == max:
    flag = 0
  elif distance == min:
    flag = 1
