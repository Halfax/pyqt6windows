import random


def roll_high(sides, times):
    high_roll = 0
    for _ in range(times):
        roll = random.randint(1, sides)
        if roll > high_roll:
            high_roll = roll
    return high_roll

def roll_low(sides, times):
    low_roll = sides + 1
    for _ in range(times):
        roll = random.randint(1, sides)
        if roll < low_roll:
            low_roll = roll
    return low_roll

def roll_dice(sides, times):
    total = 0
    for _ in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total