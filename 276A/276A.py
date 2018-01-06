#http://codeforces.com/problemset/problem/276/A
inp = list(map(int, input().split()))
num, time = inp[0] , inp[1]
lis = []
hap = -100000000000000000
for x in range (num):
	temp = list(map(int,input().split()))
	lis.append(temp)

for x in lis:
	temp = x[0] -(x[1]-time)
	if x[1]<=time and  hap < x[0]:
		hap = x[0]
	if ( temp > hap and x[1] > time):
	 	hap = temp		
print(hap)
