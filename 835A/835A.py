#http://codeforces.com/problemset/problem/835/A
s,v1,v2,t1,t2 = map(int, input().split() )
ans1 = ( (2*t1) + (s*v1))
ans2 = ( (2*t2) + (s*v2))
if(ans1<ans2):
	print("First")
elif(ans1>ans2):
	print("Second")
else:
	print("Friendship")