# Playing around with Pytest.

from cake_thief import cake_heist_calculator

capacity = 100
raw_cakes_1 = [(100, 60)]
raw_cakes_2 = [(100, 60), (10, 0)]
raw_cakes_3 = [(100, 60), (60, 50)]
raw_cakes_4 = [(100, 60), (50, 50)]
raw_cakes_5 = [(119, 70), (100, 60), (60, 50)]
raw_cakes_6 = [(119, 70), (100, 60), (60, 50), (25, 40)]
raw_cakes_7 = [(5, 100), (20, 75), (17, 45), (5, 27), (75, 40), (45, 100), (0, 10), (10, 0), (5, 19)]

def test_one_cake():
    assert cake_heist_calculator(raw_cakes_1, capacity) == {(100, 60, 1.667): 1}
    # no errors when only one cake in bakery

def test_simple_case():
    assert cake_heist_calculator(raw_cakes_3, capacity) == {(60, 50, 1.2): 2}
    # program should substitute smaller cakes for larger, where doing so increases heist value
 
def test_zero_cake_weight():
    assert cake_heist_calculator(raw_cakes_2, capacity) == {(100, 60, 1.667): 1}
    # program should ignore cakes with zero weight. Would result in infinite solution.
    
def test_optimize_weight():
    assert cake_heist_calculator(raw_cakes_4, capacity) == {(100, 60, 1.667): 1}
    # to keep duffel light-weight, program should not substitute smaller cakes with the same aggregate value as a larger cake
    
def test_skip_lower_value_cake():
    assert cake_heist_calculator(raw_cakes_5, capacity) == {(60, 50, 1.2): 2}
    # program should not stop after an attempted substitution results in a lower heist.

def test_include_all_possible_combinations():
    assert cake_heist_calculator(raw_cakes_6, capacity) == {(100, 60, 1.667): 1, (25, 40, 0.625): 1}
    # program should continue substituting until all combinations have been tried.

def test_other_combinations():
    assert cake_heist_calculator(raw_cakes_7, capacity) == {(75, 40, 1.875): 2, (5, 19, 0.2632): 1}