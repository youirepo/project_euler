import os
import sys

summ = 0
for n in range(3,1000):
	if n%3 or n%5:
		summ += n

print summ
