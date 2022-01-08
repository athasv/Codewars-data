def triple_trouble(one, two, three):
	temp = [a+b+c for a, b,c in zip(one, two, three)]
	return "".join(temp)