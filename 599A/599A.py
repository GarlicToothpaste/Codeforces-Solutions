#http://codeforces.com/problemset/problem/599/A
d = list(map(int,input().split()))

print(min(d[0]+d[1]+d[2],2*(d[0]+d[2]),2*(d[1]+d[2]),2*(d[1]+d[0])))