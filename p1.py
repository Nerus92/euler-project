import time

def get_sum_of_3_5_multiples(max):
	multiples = [item for item in range(1, max) if any([item % 3 == 0, item % 5 == 0])]
	return sum(multiples)

if __name__ == "__main__":
	start_time = time.time()
	print get_sum_of_3_5_multiples(1000)
	print "--- %s seconds ---" % (time.time() - start_time)
