inp = int(input())
arr = [4,7,47,77,74,44,444,447,474,477,744,747,774,777]
ans = "NO"
for x in arr:
	if(inp%x == 0):
		ans = "YES"
		break
print(ans)