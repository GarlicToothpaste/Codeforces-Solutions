#http://codeforces.com/problemset/problem/837/A
_ = input()
inp = list(input().split())
arr = []
for x in inp:
	temp = sum(map(str.isupper, x))
	arr.append(temp)
print(max(arr))