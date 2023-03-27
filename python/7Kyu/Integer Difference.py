def int_diff(lst, n):
	_ = 0
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			if abs (lst[i] - lst[j]) == n:
				_ += 1
	return _