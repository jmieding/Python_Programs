"""Write a program that prints the numbers from 1 to 100, but for multiples of 3 print 
'Fizz' instead of the number, and for the multiples of 5 print 'Buzz'. For numbers that 
are multiples of both 3 and 5 print 'FizzBuzz'."""


for i in xrange(1, 101):
	if i % 5 == 0 and i % 3 == 0:
		print "FizzBuzz"
	elif i % 3 == 0:
		print "Fizz"
	elif i % 5 == 0:
		print "Buzz"
	else:
		print i