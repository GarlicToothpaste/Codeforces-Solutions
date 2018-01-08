#http://codeforces.com/problemset/problem/879/A
tCases = int(input())
appointment = []
ans = 0
for x in range(tCases):
	a,b = (map(int, input().split() ))
	ans = a+((ans-a)//b+1)*b if ans>=a else a
print(ans)