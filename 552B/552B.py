inp = int(input())
ans = 0
var = 9
ans = 0
num = 1
while inp > 0:
	ans += min(inp,var)*num
	inp -= var
	var *= 10
	num += 1
print(ans)