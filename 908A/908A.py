item = input()
digits = ["a","e","i","o","u","1","3","5","7","9"]
ans = 0
for x in item:
	if (x in digits):
		ans += 1

print (ans)