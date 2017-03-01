# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Note there is a limitation with this implementation as it is limited
# C99 long not long long which is needed for this huge number.

def is_prime(N):
	half = 0
	if not N % 2:
		return False

	half = int(N/2)
	for num in xrange(3, half):
		if not N % num:
			return False
	return True

if __name__ == '__main__':
	divisor = 2
	num = 600851475143
	factor = num

	while True:
		if not num % divisor:
			factor = num / divisor

			if is_prime(factor):
				print "%ld is the largest prime factor." % factor
				break

		divisor += 1

