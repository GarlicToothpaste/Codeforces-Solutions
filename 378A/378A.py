_ = list(map(int,input().split()))
p1,p2 = _[0] , _[1] 
p1Win = 0
draw = 0
p2Win = 0
for x in range(1,7):
	p1Dist = abs(p1-x)
	p2Dist = abs(p2-x)
	if(p1Dist<p2Dist): p1Win += 1
	elif(p1Dist>p2Dist): p2Win += 1
	else: draw+=1
print(str(p1Win) + " " + str(draw) + " " + str(p2Win))