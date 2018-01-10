#http://codeforces.com/problemset/problem/820/A
c,v0,v1,a,l = map(int, input().split())
counter = 0
while (c>0):
	c -= v0
	v0 += a
	if (v0>v1):
		v0 = v1
	counter += 1
	if(counter>=1 and c > 0):
		c += l
print(counter)