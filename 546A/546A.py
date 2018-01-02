a = list(map(int, input().split()))
ans = 0
for x in range(1,(a[2]+1)):
	ans = ans  + x*a[0]
ans = ans - a[1]
print(ans if ans > 0 else "0")