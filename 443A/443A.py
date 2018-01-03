inp = input()
inp = inp.replace("{", "").replace("}", "").replace(",","")
inp = set(inp.split(" "))
if "" in inp:
	inp.remove("")
print(0 if inp is None else len(inp))