#http://codeforces.com/problemset/problem/900/A
count= int(input())
inp = []
for x in range(count):
	inp.append(list(map(int,input().split())))

countl = 0
countr = 0
for x in inp:
	if x[0]>0:
		countr+=1
	if x[0]<0:
		countl+=1
print("Yes" if countl <= 1 or countr <= 1 else "No")