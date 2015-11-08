"""
Python 2.7.10 

Puzzle: Find the nth number in the fibonacci sequence. The nth number
can be provided by the user.

This program assumes that 0 is the "zeroth" number in the sequence and 
the first 1 is the first number.

Wrote recursive solution for kicks.

"""
# User input
# num = int(raw_input("Which number in the fibonacci sequence would you like to know? > "))

# Recursive solution.

def nth_number_in_fibonacci_sequence_recursion(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return nth_number_in_fibonacci_sequence_recursion(num - 2) + nth_number_in_fibonacci_sequence_recursion(num - 1)

# Iterative solutions

  # Prior solution used list instantiation/appending to generate fib. sequence.
  # Using integers saves between 20% - 60% on execution time according to timeit module.

def nth_number_in_fibonacci_sequence_iteration(num):
  c, a, b = 0, 0, 1
  if num > 1:
    for i in xrange(1, num):
      c = a + b
      a = b
      b = c
    return c
  elif num == 1:
    return 1
  else: 
    return 0


# OLD SOLUTION

def iteration_old(num):
  sequence = [0, 1]
  if num > 1:
    for i in xrange(1, num):
      sequence.append(sequence[-2] + sequence[-1])
    return sequence[-1]
  elif num == 1:
    return sequence[-1]
  else: 
    return sequence[0]
