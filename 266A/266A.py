_ = input()
inp = input()
inp = list(inp)
count = 0
for x in range(len(inp)-1):
	if(inp[x]==inp[x+1]):
		count += 1
print(count)