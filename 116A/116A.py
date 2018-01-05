tCases = int(input())
inp = []
maxPass = 0
currPass = 0
for x in range(tCases):
	temp = list(map(int, input().split()))
	inp.append(temp)
#print(inp)

for x in inp:
	currPass = currPass + x[1] - x[0]
	if(currPass > maxPass):
		maxPass = currPass
print(maxPass)