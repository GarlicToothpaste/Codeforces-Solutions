#http://codeforces.com/problemset/problem/879/B
inp = list(map(int,input().split() ))
games = inp[1]
players = list(map(int,input().split()))
best= players[0]
victory = 0
if(games>=len(players)-1):
 	print(max(players))
else:
	for x in players[1:]:
		if x < best:
			victory += 1
		else:
			best = x
			victory = 1
		if victory == games: break
	print(best)