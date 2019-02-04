

if __name__ == '__main__':
    cat = "That is Alice's cat"
    print(cat)

    dog = 'Say hi to Bob\'s dog'
    print(dog)

    wat = "She said \"Nah\""
    print(wat)

    thing = "Newline\n\twith a tab"
    print(thing)

    windows = "Microsoft uses \\ in path names instead of /"
    print(windows)

    print(r'Jeff\'s hat')
    print('Jeff\'s hat')

    print()

    print('''
This is how you can print 
    multi-line print
        statements
    ''')
    print("End")

    sub = "I will print a substring"
    print(sub[5:-3])

    hi = "Hello world"

    print("Hello" in hi)
    print('o'.upper() in hi)
    print('O'.lower() in hi)

    print('ME'.islower())
    print('ME'.isupper())

    while True:
        print("Enter a number")
        num = input()
        if num.isdigit():
            print(num+' is a digit')
        elif num.isdecimal():
            print(num+' is a decimal')
        elif num.isnumeric():
            print(num+' is numeric')
        elif num.isalnum():
            print(num+' is a alphanumeric')
        elif num.isalpha():
            print(num+' is just a normal string')
        else:
            print('indeterminable:', type(num))
