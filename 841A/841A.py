#http://codeforces.com/problemset/problem/841/A
n,k = map(int, input().split())
balloons= input()
balloons = list(balloons)
dic = {}
for x in balloons:
	if x in dic:
		dic[x] += 1
	else:
		dic[x] = 1
if(int(max(dic.values()))>k):
	print("NO")
else:
	print("YES")