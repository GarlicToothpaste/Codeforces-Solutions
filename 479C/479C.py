#http://codeforces.com/problemset/problem/479/C
inp = int(input())
scheds = []
ans = 0
for x in range(inp):
	temp = list(map(int, input().split()))
	scheds.append(temp)
scheds.sort()
#print(scheds)
for a,b in scheds:
	if b < ans:
		ans = a
	else:
		ans = b
print(ans)