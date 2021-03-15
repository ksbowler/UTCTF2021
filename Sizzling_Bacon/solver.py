c = "sSsSSsSSssSSsSsSsSssSSSSSSSssS{SSSsSsSSSsSsSSSsSSsSSssssssSSSSSSSsSSSSSSSSsSSsssSSssSsSSSsSSsSSSSssssSSsssSSsSSsSSSs}"
i = 0
while i < len(c):
	if c[i] == '{':
		print("{",end="")
		i += 1
		continue
	if c[i] == '}':
		print("}")
		break
	s = ""
	for j in range(i,i+5):
		if c[j] == 's': s += "1"
		else: s += "0"

	print(chr(int(s,2)+ord('a')),end="")
	i += 5
