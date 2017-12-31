_ = input()
inp = input()
inp = list(inp)
prev = inp[0]
sfcount = 0
fccount = 0
for x in inp[1:]:
	if(prev == "S" and x == "F" ):
		sfcount += 1
		prev = x
	if(prev == "F" and x == "S"):
		fccount += 1
		prev = x
	else:
		prev = x
print("YES" if (sfcount > fccount) else "NO")