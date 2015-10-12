# Python 2.7.10
# This program calculates the future value of a given amount with compounding interest.

print "\nFuture Value Calculator\n"

principal = float(raw_input("How much $ are you starting with? "))
annual_interest_rate = float(raw_input("What is your annual interest rate? (For example, enter .04 for 4%) "))
times_compounded = int(raw_input("How many times will interest compound in each year? "))
years = int(raw_input("How many years will interest compound?\n "))

# Simple Solution

total = principal * (1 + (annual_interest_rate/times_compounded)) ** years
print "\nSimple Solution: ", format(total, '.2f')

# Iterative solution

def compound_interest_iterative(principal, annual_interest_rate, times_compounded, years):
  total = principal
  for i in range(1, years + 1):
      total += total * (annual_interest_rate/times_compounded)
  print "\nIterative Solution:", format(total, '.2f')

compound_interest_iterative(principal, annual_interest_rate, times_compounded, years)

# Recursive solution

def compound_interest_recursive(principal, annual_interest_rate, times_compounded, years):
  if years == 0:
    return principal
  else:
    return (1 + (annual_interest_rate/times_compounded)) * compound_interest_recursive(principal, annual_interest_rate, times_compounded, years - 1)

total = compound_interest_recursive(principal, annual_interest_rate, times_compounded, years)
print "\nRecursive Solution: ", format(total, '.2f')