#http://codeforces.com/problemset/problem/268/B
number = input()
number = int(number)
ans = 0
for x in range(number):
	ans += x*(number-x)
ans +=  number

print(ans)
