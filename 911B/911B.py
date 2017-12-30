#http://codeforces.com/problemset/problem/911/B
plate, c1, c2 = [int(i) for i in input().split(" ")]
ans = 0
for x in range(1,plate):
	ans = max(ans, min(c1//x , c2//(plate-x)))
print(ans)