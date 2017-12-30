#http://codeforces.com/problemset/problem/893/A
count = int(input())
games = []

for x in range(count):
	games.append(int(input()))
state = "YES"
play = [1,2]
for x in games:
	if x in play:
		play = [x, 6-(play[0]+play[1])]
	else:
		state = "NO"
		break
print(state)