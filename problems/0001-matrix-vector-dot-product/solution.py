def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	result = []
	for i in range(len(a)):
		entry = 0
		for j in range(len(a[0])):
			entry += a[i][j] * b[j]
		result.append(entry)
	return result
	