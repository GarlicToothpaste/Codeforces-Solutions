#http://codeforces.com/problemset/problem/703/A
tCases = int(input())
results = []
mWin = 0
cWin = 0
for x in range(tCases):
	temp = list(map(int, input().split() ))
	results.append(temp)
for x in results:
	if x[0] > x[1]:
		mWin += 1
	elif x[0] < x[1]:
		cWin += 1
if(mWin>cWin):
	print("Mishka")
elif(mWin< cWin):
	print("Chris")
else:
	print("Friendship is magic!^^")