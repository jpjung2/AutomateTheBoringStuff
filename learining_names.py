names = []

while True:
    name = input("What is your name? ")
    if name not in names:
        print("Hmmm, I haven't heard that name before. Nice to meet you, {}!".format(name))
        names.append(name)
    else:
        print("{}! I recognize that name!".format(name))
