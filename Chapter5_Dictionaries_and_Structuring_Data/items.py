"""
    This was more or less an experiment to see what is returned by the dict.items() function

    Turns out, it returns a key an value pair at the most

    So a for in loop will allow at most 2 iterators
        for a,b in dict.items()
            ...

    Iterating items() with a single variable will return a tuple/set for that variable:
        for a in dict.item()
            ...
"""

if __name__ == '__main__':
    d = {"Jeff": {"Car": {"Make": "Scion", "Model": "tC", "Year": 2008}},
         "Adam": {"Car": {"Make": "Chevy", "Model": "Cruze", "Year": 2011}},
         "Sean": {"Car": {"Make": "Ford", "Model": "Escape", "Year": 2014}}}

    for a in d.items():
        print(type(a), a)

    print()

    for a, b in d.items():
        print(type(a), a)
        print(type(b), b)
        print()
