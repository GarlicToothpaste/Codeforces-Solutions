#http://codeforces.com/problemset/problem/912/A
inp = list(map(int, input().split()))
output = list(map(int,input().split()))
YellowNeed, BlueNeed = 0 , 0
YellowNeed = max(((output[0]*2)+output[1])-inp[0],0)
BlueNeed = max((output[1]+(output[2]*3))-inp[1],0)
ans = YellowNeed+BlueNeed
print(ans)