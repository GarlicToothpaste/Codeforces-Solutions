#http://codeforces.com/problemset/problem/231/A

tCases = int(input())
count= 0
num = []
for x in range(tCases):
	a = list(map(int,(input().split())))
	num.append(a)
	if(sum(num[x])>=2):
		count+= 1
print(count)