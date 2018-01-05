_ = int(input())
#inp = list(map(int,input().split()))
testInp = input().split(" ")
origInp = list(map(int,testInp))
SorInp = list(map(int,testInp))
SorInp.sort()

goods = 0
rev = _-1

count = 0
if SorInp==origInp:
	print("yes")
	print("1 1")
else:
	while origInp[goods]==SorInp[goods]:
		goods += 1
	while origInp[rev] == SorInp[rev]:
		rev -= 1
	if origInp[goods:rev+1] == SorInp[goods:rev+1][::-1]:
		print("yes")
		print(1+min(goods,rev),1+max(goods,rev))
	else:
		print("no")