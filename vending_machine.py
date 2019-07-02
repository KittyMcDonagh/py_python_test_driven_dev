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

# Note: The program will go through the coin loop one after the other. When the
# amount is changed, the next coin it picks from the list, is the one after the
# last one it checked. So if we use 9 as the amount, the first coin to be 
# appended will be the 5, amount will be reduced to 4; next coin picked up will
# be 2, amount will be reduced to 2; next coin to be picked up will be 1. So it
# will return 5, 2, 1 for 9, instead of 5, 2, 2.

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
test_are_equal(get_change(9), [5, 2, 2])





print ("All tests pass!")

