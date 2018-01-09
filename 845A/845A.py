#http://codeforces.com/problemset/problem/845/A
n = int(input())
players = list(map(int, input().split()))
ans = 0
team1 = []
for x in range(n):
	big = max(players)
	ans += big
	team1.append(big)
	players.remove(big)
if( ans > sum(players) and max(players)<min(team1)):
	print("YES")
else:
	print("NO")