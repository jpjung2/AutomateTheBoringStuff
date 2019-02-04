"""
    Took first example of myCat dictionary and made it a little more complicated. Already aware of nested dictionaries
    so I just applied that here for a more challenging example of a dictionary
"""

myCat = {'size': 'skinny', 'color': 'gray', 'age': {'unit': 'months', 'value': 8}}

print(myCat)

print(myCat['age'])

print(type(myCat['age']))

for part in myCat['age']:
    print(part, ':', myCat['age'][part])
