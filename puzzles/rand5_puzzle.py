"""
Python 2.7.10

Premise: Given a function rand5() that generates random integers
from 1 - 5, write a function rand7() that generates random 
integers from 1 - 7.

"""

import timeit
import random

def rand5():
	return random.randrange(1, 6)

def rand7():
	
	conversion = 0
	
	for i in xrange(6):
		conversion += rand5()
	conversion -= 1
	# adjusts range of outcomes from 6 - 30 to 5 - 29. After adjustment,
	# there are an equal number of outcomes higher and lower than the 
	# target range, preventing the function from weighting some numbers.

	if conversion in xrange(7, 28):
		conversion = (conversion % 7) + 1
	else:
		rand7()
	# theoretically, this could result in a stack overflow, but the odds
	# of that happening are close to zero. The probability of recursively 
	# calling rand7() 3 times in a row is (4/30)^3, or about 0.2%. While
	# loop is an alternative, but it didn't consistently increase speed,
	# so I chose to leave it.

	return conversion

# Test for even distribution
def test_rand7(times):
	
	results = {
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
	}

	for i in xrange(times):
		results[(rand7() % 7) + 1] += 1

	print results

# times = 1000000
test_rand7(times)
