### This program is designed to solve a programming puzzle called "Cake Thief." You can find this and other programming puzzles at Interviewcake.com.

### Premise: a thief is breaking into a bakery to steal cakes. There are a finite number of cake types (cheese cake, chocolate cake, etc.), but each type has an infinite number of cakes. All stolen cakes must fit in a duffel bag. The duffel bag can hold an infinite volume, but can only hold a finite amount of weight. The challenge is to write a function that returns which cakes, if stolen, will result in the most valuable heist, given 1) a list [array] of tuples with two values, where the first value is an integer representing the $ value of the cake, and the second is an integer representing the weight in lbs. of the cake; and 2) a max weight that the duffel bag can hold in pounds. Weights and values may be any non-negative integer, including zero.

from decimal import *
getcontext().prec = 4

def cake_heist_calculator(raw_cakes, capacity): 
  remove_list = []
  duffel = []  
  cakes_with_ratio = []  

# Calculate cakes with highest $/lbs ratio and include the ratio as the third value of each tuple. Create a new list duffel to hold new tuples. Exclude from the new list cakes heavier than the max capacity of the bag, and cakes that weigh zero (these would fit in the bag an infinite number of times). Sort this list from highest $/lbs to lowest.
 
  for tup in raw_cakes:
    if tup[1] <= capacity and tup[1] > 0 and tup[0] > 0:
      cakes_with_ratio.append((tup[0], tup[1], float(Decimal(tup[0]) / Decimal(tup[1]))))
    else:
      raw_cakes.pop(raw_cakes.index(tup)) 
  cakes_sorted_by_ratio = sorted(cakes_with_ratio, key= lambda tup: tup[-1], reverse=True) 
  
 # Start adding cakes beginning with the type with the highest $/lbs. Add as many cakes of that type as possible. When no more fit, do the same for the type with next highest ratio, and so on until the duffel cannot hold another cake.
 
  for tup in cakes_sorted_by_ratio:
    while capacity >= tup[1]:
      duffel.append(tup)
      capacity -= tup[1]

# If the bag is full, great! This is the optimal solution. Print the cakes included in the duffel. Use a dictionary for readability.
  
  if capacity == 0 or len(cakes_sorted_by_ratio) < 2:
    return final_view(duffel)
    
# If the bag is not full, it is possible that there is a better solution. For example, suppose bag capacity is 100lbs, and there are two types of cakes: ($100, 60lbs), ($60, 50lbs). Without more code, the program will return one ($100, 60lb) cake as the optimal solution because it has the highest $/lbs ratio, leaving the thief with a heist of $100, when the optimal solution is two cakes with a slightly lower $/lbs ratio ($60, 50lbs) resulting in a heist of $120.

#  My code for this problem gets a little elaborate, but the concept is simple. First, evaluate whether replacing the heaviest cake in the bag with a combination of lighter cakes increases the heist value. Start with the next lightest cake with the cake with the highest $/lbs ratio working down until the bag cannot hold another cake. If replacing the heavier cake results in a larger heist, then remove the heavy cake from the bag, add the lighter cakes, and repeat the process with the next heaviest cake. Repeat until BOTH a substitution results in a heist value <= the heavier cake AND you have checked all possible combinations of lighter cakes for that substitution. Terminating the program after ONLY checking for a substitution that results in a lower value may not give you the best solution. See test_skip_lower_value_cake.

  else:
    duffel = sorted(duffel, key= lambda tup: tup[1], reverse=True)
    capacity += sum(y for x, y, z in duffel) # reset capacity to empty duffel
    for tup in duffel:
      capacity -= sum(y for x, y, z in duffel[(duffel.index(tup) + 1):]) # capacity of the bag without the heaviest cake
      temp_heist = 0
      better_cakes = []
      cake_check(cakes_sorted_by_ratio, tup, duffel, better_cakes, temp_heist, capacity, remove_list)
    return final_view(duffel)

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
    # Skip over a cake if it is identical to the cake removed or if it won't fit in the remaining duffel capacity.
    if cake[1] >= tup[1] or cake[1] > capacity:
      pass
    # if a cake fits, add as many as possible      
    else:
      while capacity >= cake[1]:
        better_cakes.append(cake)
        capacity -= cake[1]
        temp_heist += cake[0]

# If the replacements are a higher value than the original cake, 1) add the replaced cake to a temporary list (remove_list) to avoid deleting an item in the duffel while iterating over it. After the iteration is complete, everything that is in both the remove_list and the duffel will be removed from the duffel. 2) Add the replacement cakes to the duffel.
 
  if tup[0] < temp_heist:
    remove_list.append(tup)
    for cake in better_cakes:
      duffel.append(cake)
   
# if the combination of replacements is not as valuable as the original cake, remove the first cake from the combination and attempt to substitute again.      
  elif tup[0] > temp_heist and better_cakes: 
    for cake in better_cakes:
      capacity += better_cakes[0][1] #reset capacity to reflect removing the would-be substitutes
      temp_heist -= better_cakes[0][0] # reset temp_heist to reflect removing the would-be substitutes
    try:
      cakes_sorted_by_ratio.pop(cakes_sorted_by_ratio.index(better_cakes[0]))
    except ValueError: # if cake in substitute cake has already been removed from sorted_cakes, pass
      pass
    better_cakes = []
    cake_check(cakes_sorted_by_ratio, tup, duffel, better_cakes, temp_heist, capacity, remove_list)
    
# if there are no potential substitutes that can fit into the remaining capacity, then all combinations have been tried and there is not better solution. Remove any cakes from duffel that have been replaced and convert the to dictionary for readability.    
  else:
    if remove_list:
      for item in remove_list:
        if item in duffel:
          duffel.pop(duffel.index(item))
    else:
      pass
    return final_view(duffel)