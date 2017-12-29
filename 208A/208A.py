#http://codeforces.com/problemset/problem/208/A
string = input().split("WUB")
string = list(filter(None, string))
ans = ""
for s in string:
	 ans += (s + " ")
print (ans)