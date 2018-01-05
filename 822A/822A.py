import math
inp = list(map(int, input().split()))
if(inp[0]<inp[1]):
	aFac = math.factorial(inp[0])
	print(aFac)
	exit()
else:
	bFac = math.factorial(inp[1])
	print(bFac)
	exit()
