p = 69691
g = 1001

A = 17016
B = 47643
x1 = 1
x2 = 1

while x1 < p:
	if pow(g,x1,p) == A:
		print("x1:",x1)
	x1 += 1

while x2 < p:
	if pow(g,x2,p) == B:
		print("x2:",x2)
	x2 += 1
