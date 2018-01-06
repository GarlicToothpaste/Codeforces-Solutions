_ = input()
inp = list(map(int,input().split()))
dic = {25:0, 50:0, 100:0}
stat = False
for x in inp:
	stat = False
	if(x==25):
		dic[x] += 1
		stat = True
	elif(x==50 and dic[25]>= 1):
		dic[x] += 1
		dic[25] -= 1
		stat = True
	elif(x==100):
		if(dic[50]>=1 and dic[25]>= 1 ):
			dic[25] -= 1
			dic[50] -= 1
			dic[x] +=1
			stat = True
		elif(dic[25]>=3):
			dic[x]+= 1
			dic[25]-= 3
			stat = True

	if(stat == False):
		print("NO")
		exit()
print("YES")