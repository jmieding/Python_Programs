"""
Python 2.7.10

Euler Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""

def sum_square_difference(number):
  sum_of_squares = 0
  square_of_sum = 0
  for num in xrange(1, number + 1):
    sum_of_squares += num * num
    square_of_sum += num
  square_of_sum *= square_of_sum
  return square_of_sum - sum_of_squares

print sum_square_difference(10)
print sum_square_difference(3)
print sum_square_difference(100)