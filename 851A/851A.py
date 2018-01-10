#http://codeforces.com/problemset/problem/851/A
n,k,t = map(int, input().split() )
print (min(t,k,n+k-t))