#http://codeforces.com/problemset/problem/877/A
name = input()
dCount = name.count("Danil")
nCount = name.count("Nikita")
oCount = name.count("Olya")
sCount = name.count("Slava")
aCount = name.count("Ann")
ans = dCount +nCount+ oCount+ sCount+aCount
if(ans == 1):
	print ("YES")
else:
	print("NO")