#http://codeforces.com/problemset/problem/581/A
inp = list(map(int, input().split() ))
red, blue = inp [0], inp[1]
hipCount = 0
regCount = 0
while (True):
	if(red>= 1 and blue >= 1):
		red -= 1
		blue -= 1
		hipCount += 1
	elif(red>=2):
		red -= 2
		regCount += 1
	elif(blue>= 2):
		blue -= 2
		regCount += 1
	else:
		break
print(hipCount, regCount)