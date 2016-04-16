import time

def fibonacci_up_to(max):
	fibonacci = [1, 2]
	next = 3
	while next < max:
		fibonacci.append(next)
		next = fibonacci[-1] + fibonacci[-2]
	return fibonacci

def sum_even_valued_fibonacci_terms(max):
	fibonacci = fibonacci_up_to(max)
	fibonacci = [element for element in fibonacci if element % 2 == 0]
	return sum(fibonacci)

if __name__ == "__main__":
	start_time = time.time()
	print sum_even_valued_fibonacci_terms(4000000) 
	print "--- %s seconds ---" % (time.time() - start_time)
