#http://codeforces.com/problemset/problem/466/A
inp = list(map(int, input().split() ))
n,m,a,b = inp[0] , inp[1] , inp[2] , inp[3] 
# n = # rides, m = # of rides for special ticket 
# a = # cost of single journey, b = cost of special ticket
print(n//m*min(b,m*a)+min((n%m)*a,b))