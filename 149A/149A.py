#http://codeforces.com/problemset/problem/149/A
n = int(input())
k = list(map(int, input().split()))
arr = []
ans = 0
count = 0
if(sum(k)<n):
	print (-1)
	exit()
while (ans<n):
	ans += max(k)
	k.remove(max(k))
	count += 1
print(count)