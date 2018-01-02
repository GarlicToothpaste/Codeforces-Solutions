_ = input()
inp = list(map(int, input().split()))
eCount = 0
oCount = 0
lastE = -1
lastO = -1
for x in range(len(inp)):
	if inp[x]%2 == 0:
		eCount += 1
		lastE = x+1
	else:
		oCount += 1
		lastO = x+1
	if (eCount >= 2 or oCount >=2) and (lastO != -1 and lastE != -1):
		break
print(lastO if eCount>oCount else lastE)