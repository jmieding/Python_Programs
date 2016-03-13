# sort array randomly
# Python 2.7.10

import random

def sort(arr):
  if arr:
    new = []
    # create list of nums that will serve as indices of our input array.
    indices = range(len(arr))
    while len(indices) > 0:
      index_selection = random.choice(indices)
      # once the index number has been randomly selected, delete it
      # to prevent it being selected twice.
      indices.pop(indices.index(index_selection))
      new.append(arr[index_selection])
    return new
  else:
    return arr, "array cannot be null"

a = [1, 2, 3, 4, 5]

print sort(a)