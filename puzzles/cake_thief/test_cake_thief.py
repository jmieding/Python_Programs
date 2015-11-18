# Playing around with Pytest.

from cake_thief import cake_heist_calculator

capacity = 100
raw_cakes_1 = [(100, 60)]
raw_cakes_2 = [(100, 60), (10, 0)]
raw_cakes_3 = [(500, 101), (60, 50)]
raw_cakes_4 = [(100, 60), (60, 50)] 
raw_cakes_5 = [(100, 60), (50, 50)]
raw_cakes_6 = [(500, 101), (100, 60), (60, 50), (50, 50), (10, 0)]

def test_one_cake():
    assert cake_heist_calculator(raw_cakes_1, capacity) == {(100, 60): 1}
    # no errors when only one cake in bakery

def test_exclude_cakes_with_zero_weight():
    assert cake_heist_calculator(raw_cakes_2, capacity) == {(100, 60): 1}
    # If failed, would result in infinite solution.

def test_exclude_cakes_heavier_than_bag_capacity():
    assert cake_heist_calculator(raw_cakes_3, capacity) == {(60, 50): 2}
    # self explanatory
 
def test_find_highest_value_combination():
    assert cake_heist_calculator(raw_cakes_4, capacity) == {(60, 50): 2}
    # when the value of a single cake is exceeded by the combined value of smaller cakes, 
    # program should return the combination of smaller cakes.

def test_optimize_weight():
    assert cake_heist_calculator(raw_cakes_5, capacity) == {(100, 60): 1}
    # when two or more combinations are of equal value, program should return
    # cake combination with lightest weight.

def test_combine_all_tests():
    assert cake_heist_calculator(raw_cakes_6, capacity) == {(60, 50): 2}
    