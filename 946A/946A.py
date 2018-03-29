#http://codeforces.com/problemset/problem/946/A

tCases = input()
lis = list(map(int, input().split()))
b,c = 0 , 0
for x in lis:
	if(x >= 0):
		b += x
	else:
		c += x
print(b-c)