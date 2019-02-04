"""
    Took first example of myCat dictionary and made it a little more complicated. Already aware of nested dictionaries
    so I just applied that here for a more challenging example of a dictionary
"""

def recursive_dict(d):
    for item in d:
        if type(d[item]) is dict:
            print("Entering dictionary", item)
            recursive_dict(d[item])
        else:
            print(item, ":", d[item])


myCat = {'size': 'skinny', 'color': 'gray', 'age': {'unit': 'months', 'value': 8}}

print(myCat)

print(myCat['age'])

print(type(myCat['age']))


recursive_dict(myCat)

