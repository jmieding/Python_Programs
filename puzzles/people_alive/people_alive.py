""""
This program uses python 2.7.10.

Puzzle: given a list of names and dates that people lived during the period of 1900-1999, 
return the year in which the most people in the list were alive. For people still living, there will 
only be a birth year. E.g., ["Tim", 1985, "Gerald", ...]. 
"""

import re

dates_lived = []

table = {}
for year in xrange(1900, 2000):
  table[year] = 0

# names_dates = ["carl smith", 1967, "ted jones", 1900, 1970, "john michaels", 1971, 1985, "tim burton", 1990]
# uncomment to use default inputs

def main(names_dates):

# extract all dates from list

  names_dates = str(names_dates)
  dead = re.findall(r'[0-9]+, [0-9]+', names_dates)
  alive = re.findall(r'[^0-9], [0-9]+, [^0-9]', names_dates)

# convert dates to integers, include in new list

  for person in dead:
    dates_lived.append((int(person[0:4]), int(person[6:10])))
    
  for person in alive:
    dates_lived.append((int(person[3:7]), 1999))

# for each year that a person is alive, add 1 to the value.

  for years_alive in dates_lived:
    for year in xrange(years_alive[0], years_alive[1] + 1):
      table[year] += 1
      
  table_sorted = sorted(table.items(), key=lambda year: year[1], reverse = True)
  return table_sorted
  #print table_sorted

#main(names_dates)