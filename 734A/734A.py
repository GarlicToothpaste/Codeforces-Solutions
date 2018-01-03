_ = input()
inp = input()
inp = list(inp)
aCount, dCount = 0, 0
for x in inp:
	if x == "A":
		aCount += 1
	if x == "D":
		dCount += 1
if(aCount>dCount):
	print("Anton")
elif(aCount<dCount):
	print("Danik")
else:
	print("Friendship")