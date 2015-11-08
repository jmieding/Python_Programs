import timeit

from fibonacci import(
	nth_number_in_fibonacci_sequence_recursion,
	nth_number_in_fibonacci_sequence_iteration,
	iteration_old 
)

num1 = 10
num2 = 20
num3 = 30
num4 = 100

def test_check_recursive_math():
	assert nth_number_in_fibonacci_sequence_recursion(num1) == 55
	# Don't run these tests unless you want to wait a loooooong time.
	# assert nth_number_in_fibonacci_sequence_iteration(num2) == 6765
	# assert nth_number_in_fibonacci_sequence_iteration(num3) == 832040
	print "\n\nRecursive time: \n %0.7f" % (timeit.timeit(
		lambda: nth_number_in_fibonacci_sequence_recursion(num1),
		number = 1000)
	)

def test_check_iterative_math():
	assert nth_number_in_fibonacci_sequence_iteration(num1) == 55
	assert nth_number_in_fibonacci_sequence_iteration(num2) == 6765
	assert nth_number_in_fibonacci_sequence_iteration(num3) == 832040
	print "\n\nIterative time: \n %0.7f" % (timeit.timeit(
		lambda: nth_number_in_fibonacci_sequence_iteration(num1),
		number = 1000)
	)
	print "\nOld Iterative time: \n %0.7f" % (timeit.timeit(
		lambda: iteration_old(num1),
		number = 1000)
	)