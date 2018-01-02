tC = int(input())
inp = []
count = 0
for x in range(tC):
	temp =list(map(int, input().split()))
	inp.append(temp)

	if((inp[x][0])<=(inp[x][1]-2)):
		count +=1
print(count)