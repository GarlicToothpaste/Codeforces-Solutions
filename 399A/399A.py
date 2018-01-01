inp = input().replace("+","")
inp = list(inp)
inp.sort()
ans = ""
lisLen = len(inp)
for x in range(lisLen-1):
	ans = ans+inp[x]+"+"
ans = ans + inp[lisLen-1]
print(ans)