inp = input()
for x in range(int(inp)+1,10000):
	if len(set(str(x))) == len(str(inp)):
		print(x)
		exit()
