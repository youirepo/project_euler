"""Multiples of 3 and 5

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

summ = 0
for n in xrange(3, 1000):
	if not n%3 or not n%5:
		summ += n
	
print summ
