def fact(n, factorial = 1):
	if n == 1:
		return factorial
	return fact(n-1, factorial*n)