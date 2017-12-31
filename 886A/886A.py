#http://codeforces.com/problemset/problem/886/A
inp = list(map(int, input().split(" ") ))
out = "NO"
half = sum(inp)/2
state = "NO"
for i in range(1,5):
	for j in range(i+1,6):
		temp = inp[0] + inp[i] + inp[j]
		if(temp == half):
			state="YES"

print(state)
