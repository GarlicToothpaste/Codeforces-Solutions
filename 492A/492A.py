#http://codeforces.com/problemset/problem/492/A
inp = int(input())
count = 0
sub = 1
num = 1
while inp > 0 and inp >= sub:
	inp -= sub
	num += 1
	sub += num
	count += 1

print (count)