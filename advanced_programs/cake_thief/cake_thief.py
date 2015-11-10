
"""
Python 2.7.10

This program is designed to solve a programming puzzle called "Cake Thief." 
You can find this and other programming puzzles at Interviewcake.com.

Premise: a thief is breaking into a bakery to steal cakes. There are a finite 
number of cake types (cheese cake, chocolate cake, etc.), but each type has an 
infinite number of cakes. All stolen cakes must fit in a duffel bag. The duffel 
bag can hold an infinite volume, but can only hold a finite amount of weight. 
The challenge is to write a function that returns which cakes, if stolen, will 
result in the most valuable heist, given 1) a list of tuples with two 
values, where the first value is an integer representing the value in dollars($) of 
the cake, and the second is an integer representing the weight in lbs. of the cake; 
and 2) a max weight that the duffel bag can hold in pounds. Weights and values may 
be any non-negative integer, including zero.
"""

from itertools import combinations_with_replacement

def cake_heist_calculator(raw_cakes, capacity):
# define function to return optimal cake heist given a list of cakes and duffel capacity
  
  eligible_cakes = [] 
  # stores cakes that meet criteria below. See comment in "for cake in raw_cakes" loop.
  for cake in raw_cakes:
    if 0 < cake[1] <= capacity and cake[0] > 0: 
    # cakes must be heavier than 0lbs., but lighter than bag capacity, and must be
    # worth more than $0.
      eligible_cakes.append(cake)
    else:
      pass

  all_combinations = [] # stores all combinations of cakes that do not exceed bag capacity.
  smallest_cake = min(eligible_cakes, key= lambda cake: cake[1])[1]
  # this value is used to calculate the max number of cakes allowed in a combination

  for combination_length in xrange(1, int(capacity/smallest_cake)+1):
  # each value is a possible number of cakes in a combination
    for combination in combinations_with_replacement(eligible_cakes, combination_length):
    # each value is a tuple of tuples
      if sum(weight for value, weight in combination) > capacity:
        pass
      # if the combination weight > capacity, ignore it.
      else:
        all_combinations.append(combination)
      # collect all combinations that fit within bag capacity

  best_combination = max(all_combinations, key= lambda combination: sum(value for value, weight in combination))
  # find highest value combination.

  best_combination_dict = {}
  for cake in best_combination:
    if cake in best_combination_dict:
      best_combination_dict[cake] += 1
    else: 
      best_combination_dict[cake] = 1
  return best_combination_dict
  # convert to Dictionary for readability. I don't care about cake order, so it's faster than built-in Counter() function.