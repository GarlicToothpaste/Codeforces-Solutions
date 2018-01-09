#http://codeforces.com/problemset/problem/785/A
tCases = int(input())
count = 0
for x in range(tCases):
	temp = input()
	if temp == "Icosahedron":
		count += 20
	elif temp == "Cube":
		count += 6
	elif temp == "Octahedron":
		count += 8
	elif temp == "Dodecahedron":
		count += 12
	elif temp == "Tetrahedron":
		count += 4
print(count)