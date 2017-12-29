#http://codeforces.com/problemset/problem/888/B
lenght = input()
moves = input()
print((min(moves.count("U"),moves.count("D"))*2)+(min(moves.count("L"),moves.count("R"))*2))
