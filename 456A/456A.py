#http://codeforces.com/problemset/problem/456/A

_ = int(input())
inp = []
hapCount = 0
porCount = 0
for x in range(_):
	x = list(map(int, input().split()))
	inp.append(x)

for x in inp:
	if(x[0] != x[1]):
		print("Happy Alex")
		exit()
print("Poor Alex")