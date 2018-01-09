#http://codeforces.com/problemset/problem/844/A
string = input()
k = int(input())

string = list(string)
unique = set(string)

if(k <= len(string)):
	if(k>= len(unique)):
		print(k-len(unique))
	else:
		print(0)
else:
	print("impossible")