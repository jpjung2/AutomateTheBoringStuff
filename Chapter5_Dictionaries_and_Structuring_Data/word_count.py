"""
    Like the example in the chapter, counts the number of each unique character
"""


def count(msg):
    res = {}
    for ch in str(msg):
        if ch not in res:
            res.setdefault(ch, 0)

        res[ch] += 1
    return res


if __name__ == '__main__':
    print("Type something and I'll count the number of each unique character")
    while True:
        message = input()
        result = count(message)
        print(result)
        print()
        print("Again!!!")
