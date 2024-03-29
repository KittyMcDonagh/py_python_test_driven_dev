"""
The specification for this program: Given the amount of change that needs to be
paid, generate the list of coins that needs to be given to the customer.
The function should pay the minimum amount of coins possible and the coin  
denominations are 100, , 20, 10, 5, 2, 1.
"""

# Import the test framework

from byotest import *

# eur_coins = [100, 50, 20, 10, 5, 2, 1]

eur_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20} 
eur_coins_qty = {100: 0, 50: 1, 20: 2, 10: 2, 5: 2, 2: 1, 1: 1} 

# usd_coins = [100, 50, 25, 10, 5, 1]
usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20} 

error_mesg = "Not enough coins available. Amount owed {} cents."



# "coins=eur_coins" makes this an optional argument. If an argument isnt 
# supplied it defaults to eur_coins.

def get_change(amount, coins=eur_coins):
    

# Note: The program will go through the coin loop one after the other. When the
# amount is changed, the next coin it picks from the list, is the one after the
# last one it checked. So if we use 9 as the amount, the first coin to be 
# appended will be the 5, amount will be reduced to 4; next coin picked up will
# be 2, amount will be reduced to 2; next coin to be picked up will be 1. So it
# will return 5, 2, 1 for 9, instead of 5, 2, 2. 
# To fix this change "if coin <= amount:" to "while coin <= amount:"

    change = []
    for coin in sorted(coins.keys(), reverse=True):
        print("amount: ", amount, "coin: ", coin, "qty: ", coins[coin])
        while coin <= amount and coins[coin] > 0:
            amount -= coin
            coins[coin] -= 1
            change.append(coin)

    if amount != 0:
        return error_mesg.format(amount)
        
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100, eur_coins_qty), [50, 20, 20, 10])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9, eur_coins_qty), "Not enough coins available. Amount owed 1 cents.")
test_are_equal(get_change(8), [5, 2, 1])
test_are_equal(get_change(35, usd_coins), [25, 10])

print ("All tests pass!")

