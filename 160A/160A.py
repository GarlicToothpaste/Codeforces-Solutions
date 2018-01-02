tC = int(input())
coins = list(map(int, input().split()))
count = 0
currBal = 0
coins.sort()
tot = sum(coins)
for x in range (tC):
	if( currBal > tot//2):
		break
	else:
		current = (tC-1) - x
		currBal += coins[current]
		count += 1
print(count)