import random

def roll():
	die_1 = random.choice(xrange(1, 7))
	die_2 = random.choice(xrange(1, 7))
	sum = die_1 + die_2
	print "%d & %d : %d" % (die_1, die_2, sum)

while raw_input("Roll again? (y/n) ") == 'y':
	roll()