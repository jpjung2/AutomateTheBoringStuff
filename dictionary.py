prop = {"size" : 32, 'color' : 'blue', 'cats' : True}

for thing in prop.items():
    print(type(thing))

prop['size'] = 26

print()

for thing in prop.items():
    print(thing)
