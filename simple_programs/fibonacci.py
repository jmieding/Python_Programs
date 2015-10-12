# Python 2.7.10 
# Finds the nth number in the fibonacci sequence. 
# This program assumes that 0 is the "zeroth" number in the sequence and the first 1 is the first number.

num = int(raw_input("Which number in the fibonacci sequence would you like to know? "))
sequence = [0, 1]

# A recursive solution.

def nth_number_in_fibonacci_sequence_recursion(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return nth_number_in_fibonacci_sequence_recursion(num - 2) + nth_number_in_fibonacci_sequence_recursion(num - 1)

print "\nRecusive Solution:", nth_number_in_fibonacci_sequence_recursion(num)


# An iterative solution

def nth_number_in_fibonacci_sequence_iteration(num):
  if num > 1:
    for i in xrange(1, num):
      sequence.append(sequence[-2] + sequence[-1])
    print "\nIterative Solution: ", sequence[-1]
  elif num == 1:
    print "\nIterative Solution: ", sequence[-1]
  else: 
    print "\nIterative Solution: ", sequence[0]
    
nth_number_in_fibonacci_sequence_iteration(num)