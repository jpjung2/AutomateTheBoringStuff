"""
    Like dictionary_0.py, just with a nicer printing function for nested dictionaries
"""


def list_dict(d, tab=''):
    for item in d:
        if type(d[item]) is dict:
            print(tab, item, ": {")
            tab += '\t'
            list_dict(d[item], tab)
            tab = tab[:-1]
            print(tab, "}")

        else:
            print(tab, str(item), ":", str(d[item]))


myCat = {'size': 'skinny', 'color': 'gray', 'age': {'unit': 'months', 'value': 8, 'foo': {'very': 'nested'}}}

print(myCat)

print(myCat['age'])

print(type(myCat['age']))

for part in myCat['age']:
    print(part, ':', myCat['age'][part])

for thing in myCat:
    if type(myCat[thing]) is dict:
        print(thing, "is a dictionary")

print("Trying some complicated printing...")

print()


print_types(myCat)

list_dict(myCat)
