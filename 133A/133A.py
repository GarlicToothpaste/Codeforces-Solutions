inp = input()
inp = list(inp)
func = ["H","Q","9"]
state = "NO"
for x in inp:
	if(x in func):
		state="YES"
		break
print(state)