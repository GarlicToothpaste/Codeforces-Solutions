#http://codeforces.com/problemset/problem/911/A

inp = int(input())
item = list(map(int, input().split()))
m = min(item)
lis = []

for x in range (inp):
	if item[x] == m:
		lis.append(x)


lislen=len(lis)

for x in range(lislen-1):
	if x == 0 and lislen > 1:
		mindis = abs(lis[x]-lis[x+1])
	else:
		temp = abs(lis[x]-lis[x+1])
		if(mindis > temp):
			mindis = temp

print(mindis)
	