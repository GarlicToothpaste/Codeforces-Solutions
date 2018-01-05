#http://codeforces.com/problemset/status

inp = list(map(int, input().split()))
a = abs(inp[0])
b = abs(inp[1])
c = abs(inp[2])
#if(a+b==c or (a+b<=c and c-(a+b)%2==0)):
if(a+b<=c):
	if(a+b == c):
		print("Yes")
		exit()
	elif((c-(a+b))%2==0):
		print("Yes")
		exit()
	else:
		print("No")
else:
	print("No")