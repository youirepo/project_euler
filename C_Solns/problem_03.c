#include <stdio.h>

// Largest prime factor
// Problem 3
// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

#define TRUE 1
#define FALSE 0

int is_prime(long long n){
	int i;
	long long half = 0;

	if(!(n % 2))
	{
		return FALSE;
	}

	half = n / 2;
	for (i = 3; i < half; i++)
	{
		if(!(n % i))
		{
			return FALSE;
		}
	}

	return TRUE;
}

int main() {
	
	long long divisor = 2;
	long long num = 600851475143;
	long long factor = num;

	while (1)
	{
		if (!(num % divisor))
		{
			factor = num / divisor;
			if (is_prime(factor))
			{
				printf("%lld is largest prime factor.", factor);
				break;
			}
		}

		divisor++;
	}

	return 0;
}
