import math, time


def number_divisible_by_all(number, divisors):
	for divisor in divisors:
		if not number % divisor == 0:
			return False
	else:
		return True

def get_smallest_divisible_by_up_to(max):
	number = 20
	divisors = [x for x in range(2, max+1)]
	while not number_divisible_by_all(number, divisors):
		number += 20
	return number

if __name__ == "__main__":
	start_time = time.time()
	print get_smallest_divisible_by_up_to(20) 
	print "--- %s seconds ---" % (time.time() - start_time)
