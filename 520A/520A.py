alphabet = list("abcdefghijklmnopqrstuvwxyz")
_ = input()
inp = input().lower()
inp = set(inp)
print("YES" if len(inp)==len(alphabet) else "NO")