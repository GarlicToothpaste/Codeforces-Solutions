#http://codeforces.com/problemset/problem/432/A
inp = list(map(int, input().split() ))
n , k = inp[0] , inp[1]
y = list(map(int, input().split() ))
var = 5-k
count = 0
for x in y:
	if(x<=var):
		count += 1
print(count//3)