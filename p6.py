import math, time


def get_diff_sumsquare_squaresum(max):
	numbers = [x for x in range(1, max+1)]
	diff = 0
	for i in range(len(numbers)):
		for j in range(len(numbers)):
			if not i == j:
				diff += numbers[i] * numbers[j]
	return diff

if __name__ == "__main__":
	start_time = time.time()
	print get_diff_sumsquare_squaresum(100) 
	print "--- %s seconds ---" % (time.time() - start_time)
