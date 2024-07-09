carPoint = list(map(int, input().strip().split()))

k = int(input())
fw = 0
bw = 0
for i in range(k):
    fw += carPoint[i]

for i in range(k):
    bw += carPoint[len(carPoint) - i - 1]

# fw = carPoint[0] + carPoint[1] + carPoint[2]
# bw = carPoint[-1] + carPoint[-2] + carPoint[-3]

if fw > bw:
    print(fw)
else:
    print(bw)
