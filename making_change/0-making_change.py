#!/usr/bin/python3
"""
Module for making change with the minimum number of coins.
"""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession
        total (int): The total amount to make change for
    
    Returns:
        int: The fewest number of coins needed to meet total,
             or -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    
    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0

    for coin in sorted_coins:
        if total >= coin:
            count = total // coin
            coins_count += count
            total -= count * coin
            if total == 0:
                return coins_count

    return -1
