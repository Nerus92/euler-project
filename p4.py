import math, time


def get_all_multiples(max):
	return sorted(set([x*y for x in range(max-1, 1, -1) for y in range(max-1, 1, -1)]), reverse = True)

def get_largest_palindrome(max):
	multiples = get_all_multiples(max)
	for element in multiples:
		if str(element) == str(element)[::-1]:
			return element
	else:
		return 1

if __name__ == "__main__":
	start_time = time.time()
	print get_largest_palindrome(1000) 
	print "--- %s seconds ---" % (time.time() - start_time)
