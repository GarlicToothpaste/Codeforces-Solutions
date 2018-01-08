#http://codeforces.com/problemset/problem/884/A
inp = list(map(int, input().split() ))
days = inp[0]
readBook = inp[1]
time = list(map(int, input().split() ))
timRem = 0
counter = 0
for x in range(days):
	if(timRem >= readBook):
		break
	else:
		temp = 86400-time[x]
		timRem += temp
		counter += 1
print(counter)