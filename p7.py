from __future__ import division
import math, time


step = 1000000
not_prime = set()

def get_sieve_up_to(sieve, max):
	maxn = max + 1
	primes = sieve
	
	for i in range(sieve[-1], maxn):
		if i in not_prime:
			continue

		for f in range(i*2, maxn, i):
			not_prime.add(f)

		primes.append(i)

	return primes

def get_nth_prime(n):
	counter = 1
	sieve = [2]
	while len(sieve) < n:
		sieve = get_sieve_up_to(sieve, counter * step)
	return sieve[n] 

if __name__ == "__main__":
	start_time = time.time()
	print get_nth_prime(10001) 
	print "--- %s seconds ---" % (time.time() - start_time)
