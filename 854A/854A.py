#http://codeforces.com/problemset/problem/854/A
import math
n = int(input())
#Using this, A will always be <= b when even. a<b when odd
a,b = n//2 , n-n//2 
while (math.gcd(a,b)!= 1):
	a -= 1
	b += 1
print(a,b)