#http://codeforces.com/problemset/problem/230/A

inp = list(map(int,input().split()))
kirito = inp[0]
num_drg = inp[1]
alive = True
dragons = []

for x in range(num_drg):
	dragons.append(list(map(int,input().split())))

dragons.sort()

for x in range(num_drg):
	if kirito > dragons[x][0]:
		kirito += dragons [x][1]
	else:
		alive = False
		break

if alive == True:
	print("YES")
else:
	print("NO")