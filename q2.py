carPoint = list(map(int, input().strip().split()))

k = int(input())
fw = 0
bw = 0
for i in range(k):
    fw += carPoint[i]

for i in range(k):
    bw += carPoint[len(carPoint) - i - 1]

if fw > bw:
    print(fw)
else:
    print(bw)


# All given test cases passed
