#http://codeforces.com/problemset/problem/510/A
inp = list(map(int,input().split() ))
n = inp[0]
m = inp[1]
prev = 0
for x in range(1,n+1):
	if(x%2==0):
		if(prev == 0):
			print("."*(m-1) + "#")
			prev = 1
		elif(prev == 1):
			print("#" + "."*(m-1))
			prev = 0
	else:
		print("#"*m)