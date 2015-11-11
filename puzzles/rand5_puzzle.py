"""
Python 2.7.10

Premise: Given a function rand5() that generates random integers
from 1 - 5, write a function rand7() that generates random 
integers from 1 - 7.

"""

import random

results = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
	7: 0,
}

def rand5():
	return random.randrange(1, 6)

def rand7():
# should return random integer from 1- 7
	conversion = 0
	for i in xrange(6):
		conversion += rand5()
	
	conversion -= 1

	# without subtraction, range of outcomes is 6 - 30, which means
	# rand5 can produce 1 number lower and 3 numbers higher than
	# our target range. Subtraction rebalances the range so
	# that there are two numbers higher and lower than the 
	# range: 5, 6 and 28, 29. Distribution of 1 - 7, will therefore
	# be equal.

	if conversion not in xrange(7, 28):
		rand7()
	elif conversion in [7, 14, 21]:
		results[1] += 1
	elif conversion in [8, 15, 22]:
		results[2] += 1
	elif conversion in [9, 16, 23]:
		results[3] += 1
	elif conversion in [10, 17, 24]:
		results[4] += 1
	elif conversion in [11, 18, 25]:
		results[5] += 1
	elif conversion in [12, 19, 26]:
		results[6] += 1
	elif conversion in [13, 20, 27]:
		results[7] += 1
	else: 
		pass

# to check even distribution.
for i in xrange(10000):
	rand7()

print results