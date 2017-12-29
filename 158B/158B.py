#http://codeforces.com/problemset/problem/158/B
groups = input()
num = list(map(int,input().split()))
d = {1:0,2:0,3:0,4:0}
for digit in num:
	d[digit] += 1
print((max(0,d[1]-d[3])+d[2]*2+3)//4+d[3]+d[4])
