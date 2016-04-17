from __future__ import division
import math, time


def get_sieve_up_to(max):
	maxn = max + 1
	not_prime = set()
	primes = []
	
	for i in range(2, maxn):
		if i in not_prime:
			continue

		for f in range(i*2, maxn, i):
			not_prime.add(f)

		primes.append(i)

	return primes

def decompose_prime_factor(number, sieve):
	biggest = 1
	for prime in reversed(sieve):
		if (float(number) / float(prime)).is_integer():
			biggest = prime
			break
	return biggest

def get_largest_prime_factor(number):
	sieve = get_sieve_up_to(int(math.sqrt(number)))
	return decompose_prime_factor(number, sieve)

if __name__ == "__main__":
	start_time = time.time()
	print get_largest_prime_factor(6000851475143) 
	print "--- %s seconds ---" % (time.time() - start_time)
