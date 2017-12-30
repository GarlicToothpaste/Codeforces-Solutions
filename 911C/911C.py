#http://codeforces.com/problemset/problem/911/C

inp = list(map(int, input().split()))
inp.sort()
string = "NO"
if(inp.count(1)>= 1 or inp.count(2)>=2 or inp.count(3)>=3):
	string = "YES"
if(inp == [2,4,4]):
	string = "YES"
print(string)