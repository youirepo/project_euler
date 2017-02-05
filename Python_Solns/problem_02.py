import os
import sys

fib_nm1 = 1
fib_nm2 = 0
fib_n = 0
summ = 0
while fib_n <= 4000000:
	fib_n = fib_nm1 + fib_nm2

	if fib_n % 2 == 0:
		summ += fib_n

	fib_nm2 = fib_nm1
	fib_nm1 = fib_n

print "Sum of even Fibonacci elements is: ", summ
