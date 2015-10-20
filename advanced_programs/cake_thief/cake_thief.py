""" 
This program is designed to solve a programming puzzle called "Cake Thief." 
You can find this and other programming puzzles at Interviewcake.com.

Premise: a thief is breaking into a bakery to steal cakes. There are a finite 
number of cake types (cheese cake, chocolate cake, etc.), but each type has an 
infinite number of cakes. All stolen cakes must fit in a duffel bag. The duffel 
bag can hold an infinite volume, but can only hold a finite amount of weight. 
The challenge is to write a function that returns which cakes, if stolen, will 
result in the most valuable heist, given 1) a list [array] of tuples with two 
values, where the first value is an integer representing the $ value of the cake,
and the second is an integer representing the weight in lbs. of the cake; and 2) 
a max weight that the duffel bag can hold in pounds. Weights and values may be any 
non-negative integer, including zero.

"""
# set decimal precision for cake $/lb ratios
from decimal import *
getcontext().prec = 4

# define function to return optimal cake heist given a list of cakes and duffel capacity
def cake_heist_calculator(raw_cakes, capacity): 
  
  remove_list = [] # holds cakes that will be removed from duffel after substitution is complete.
  duffel = []  # holds the final heist
  cakes_with_ratio = [] # holds raw cakes with their $/lb ratios

"""
Calculate cakes with highest $/lbs ratio and include the ratio as the third 
value of each tuple. Create a new list duffel to hold new tuples. Exclude 
from the new list cakes heavier than the max capacity of the bag, and cakes 
that weigh zero (these would fit in the bag an infinite number of times). Sort 
this list from highest $/lbs to lowest.

"""
  # exclude cakes that 1) will not fit into the bag, 2) weigh zero lbs., 
  # or 3) have a value of zero or less.
  for tup in raw_cakes:
    if tup[1] <= capacity and tup[1] > 0 and tup[0] > 0:
      cakes_with_ratio.append((tup[0], tup[1], float(Decimal(tup[0]) / Decimal(tup[1]))))
    else:
      raw_cakes.pop(raw_cakes.index(tup))
  # sort qualifying cakes from highest $/lb ratio to lowest.
  cakes_sorted_by_ratio = sorted(cakes_with_ratio, key= lambda tup: tup[-1], reverse=True) 
  
 # begin adding cakes to the bag starting with the type with the highest $/lbs. 
 # Add as many cakes of that type as possible. When no more fit, do the same 
 # for the type with next highest ratio, and so on until the duffel cannot hold another cake.
  for tup in cakes_sorted_by_ratio:
    while capacity >= tup[1]:
      duffel.append(tup)
      capacity -= tup[1]

  # if the bag is full, or there are no cakes to attempt substituting, this is the optimal 
  # solution. Print the cakes included in the duffel. Use a dictionary for readability.
  if capacity == 0 or len(cakes_sorted_by_ratio) < 2:
    return final_view(duffel)

"""  
If the bag is not full, it is possible that there is a better solution. 
For example, suppose bag capacity is 100lbs, and there are two types of 
cakes: ($100, 60lbs), ($60, 50lbs). Without more code, the program will 
return one ($100, 60lb) cake as the optimal solution because it has the 
highest $/lbs ratio, leaving the thief with a heist of $100, when the optimal 
solution is two cakes with a slightly lower $/lbs ratio ($60, 50lbs) 
resulting in a heist of $120.

To avoid this, first, evaluate whether replacing the heaviest cake in 
the duffel with a combination of lighter cakes increases the heist value. 
Of the cakes with a lighter weight, start by trying the cake with the highest 
$/lbs ratio. Add as many as will fit, then do the same with the remaining cakes
until the bag cannot hold another cake. If replacing the heavier cake with the 
lighter ones results in a larger heist, then remove the heavy cake from the bag, 
add the lighter cakes, and repeat the process with the next heaviest cake. Stop 
when BOTH a substitution results in a heist value <= the heavier cake AND 
you have checked all possible combinations of lighter cakes for that substitution. 
Terminating the program after ONLY checking for a substitution that results in a 
lower value may not be the best solution. See test_skip_lower_value_cake in
test_cake_thief.py file.

"""

  else:
    duffel = sorted(duffel, key= lambda tup: tup[1], reverse=True)
    capacity += sum(y for x, y, z in duffel) # reset capacity to empty duffel. See next comment.
    for tup in duffel:
      # calculate capacity of the duffel without the heaviest cake by 
      # subtracting all other cakes from total capacity
      capacity -= sum(y for x, y, z in duffel[(duffel.index(tup) + 1):]) 
      temp_heist = 0 # combined value of would-be replacements for the heavier cake
      better_cakes = [] # cakes that fit into the void left by the heavier cake
      cake_check(cakes_sorted_by_ratio, tup, duffel, better_cakes, temp_heist, capacity, remove_list)
    return final_view(duffel)

# converts duffel from list to dictionary
def final_view(duffel):
  duffel_optimized = {}
  for tup in duffel:
    if tup in duffel_optimized:
      duffel_optimized[tup] += 1
    else: 
      duffel_optimized[tup] = 1
  return duffel_optimized

def cake_check(cakes_sorted_by_ratio, tup, duffel, better_cakes, temp_heist, capacity, remove_list):
  for cake in cakes_sorted_by_ratio:
    # skip over a replacement cake if it is identical to the cake removed or if it won't 
    # fit in the remaining duffel capacity.
    if cake[1] >= tup[1] or cake[1] > capacity:
      pass
    # if a cake fits, add as many as possible, then try the next best cake.      
    else:
      while capacity >= cake[1]:
        better_cakes.append(cake) # list that will hold combination of cakes to substitute
        capacity -= cake[1]
        temp_heist += cake[0] # used to compare value of would-be replacements a the cake in the duffel

  # if the replacements are a higher value than the original cake, 1) add the replaced cake 
  # to a temporary list (remove_list) to avoid deleting an item in the duffel while iterating 
  # over it, (After the iteration is complete, the program will remove all cakes from the duffel
  # that appear in the remove_list) and 2) add the replacement cakes to the duffel.
  if tup[0] < temp_heist:
    remove_list.append(tup)
    for cake in better_cakes:
      duffel.append(cake)
   
  # if the combination of would-be replacements is not as valuable as the original cake, and there are 
  # still possible combinations to try (i.e., better_cakes is not Null), remove the first cake from 
  # the combination and attempt to substitute again.      
  elif tup[0] > temp_heist and better_cakes: 
    for cake in better_cakes:
      capacity += better_cakes[0][1] # reset capacity to reflect removing the would-be replacements
      temp_heist -= better_cakes[0][0] # reset temp_heist to reflect removing the would-be replacements
    try:
      cakes_sorted_by_ratio.pop(cakes_sorted_by_ratio.index(better_cakes[0]))
    except ValueError: # if cake in substitute cake has already been removed from sorted_cakes, pass
      pass
    better_cakes = []
    cake_check(cakes_sorted_by_ratio, tup, duffel, better_cakes, temp_heist, capacity, remove_list)
    
  # if there are no possible combinations that can fit into the remaining capacity (i.e. better_cakes 
  # is Null), then all combinations have been tried and there is not better solution. If there are any 
  # cakes that have been replaced, remove them from the duffel. Convert the duffel to dictionary for readability.    
  else:
    if remove_list:
      for item in remove_list:
        if item in duffel:
          duffel.pop(duffel.index(item))
    else:
      pass
    return final_view(duffel)