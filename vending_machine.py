"""
The specification for this program: Given the amount of change that needs to be
paid, generate the list of coins that needs to be given to the customer.
The function should pay the minimum amount of coins possible and the coin  
denominations are 100, , 20, 10, 5, 2, 1.
"""

# Import the test framework

from byotest import *

def get_change(amount):
    if amount == 0:
        return []
       
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]
    
    change = []
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        if coin <= amount:
            amount -= coin
            change.append(coin)
        
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(15), [10, 5])
test_are_equal(get_change(25), [20, 5])




print ("All tests pass!")

