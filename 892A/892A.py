#http://codeforces.com/problemset/problem/892/A
_ = input()
cola = list(map(int, input().split(" ") ))
cap = list(map(int, input().split(" ") ))
cap.sort()
print("YES" if (cap[-1]+cap[-2] >= sum(cola)) else "NO")