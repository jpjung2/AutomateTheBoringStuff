

if __name__ == '__main__':
    temp = ['Jeff', 'Adam', 'Lauren']
    print(type(temp))

    name = 'Sean'
    foo = name.join(temp)

    print(name)
    print(temp)
    print(foo)

    delim = "|"
    print(delim.join(temp))

    state = "Missippi"
    for thing in state.split('i'):
        print(thing)
