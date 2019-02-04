"""
    From the example on nested dictionaries
"""


def totalBrought(d, thing):
    total = 0
    for k, v in d.items():
        total += v.setdefault(thing, 0)

    # This function operates by already knowing/assuming the set up as a single nested dictionary

    return total


if __name__ == '__main__':
    guests = {'Alice':{'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

    print("Number of things being brought:")
    print(" - Apples         ", totalBrought(guests, 'apples'))
    print(" - Cups           ", totalBrought(guests, 'cups'))
    print(" - Cakes          ", totalBrought(guests, 'cakes'))
    print(" - Ham Sandwiches ", totalBrought(guests, 'ham sandwiches'))
    print(" - Apple Pies     ", totalBrought(guests, 'apple pies'))
