from people_alive import main

names_dates_1 = ["carl smith", 1967, "ted jones", 1900, 1970, "john michaels", 1971, 1985, "tim burton", 1990]
names_dates_2 = ["carl smith", 1967, "carl smith", 1980, "ted jones", 1900, 1970, "john michaels", 1971, 1985, "tim burton", 1990]

def test_top_five():
  assert main(names_dates_1)[0:5] == [(1967, 2), (1968, 2), (1969, 2), (1970, 2), (1971, 2)]
  # evaluates top 5 results 

def test_identical_names():
  assert main(names_dates_2)[0:5] == [(1980, 3), (1981, 3), (1982, 3), (1983, 3), (1984, 3)]
  # if there are two or more people with the same name, program should count each individually, not person with the earlier list index position multiple times.