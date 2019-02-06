import re

def isPhoneNumber(text):
    pregex = re.compile(r'\d{3}-\d{3}-\d{4}')

    result = pregex.search(text)
    if result is None:
        return None
    return result.group()


if __name__ == '__main__':

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    print("Message is : \"", message,"\"")
    res = isPhoneNumber(message)
    if res is not None:
        print("Number found:", res)

    new_message = "Tacos"
    res = isPhoneNumber(new_message)
    if res is not None:
        print("Number found:", res)

    new_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = new_regex.search('my number is 415-555-9999')

    for meh in mo.groups():
        print(meh)

    print(len(mo.groups()))

    capital = re.compile(r'\S*[M|m]an')
    res = capital.search('Superheroes Batman and Robin')
    if res is not None:
        print(res.group(0))
    else:
        print("result is None")

    res = capital.search('Spider-Man')
    if res is not None:
        print(res.group(0))
    else:
        print("result is None")

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    pnum = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
    found = pnum.findall(message)
    for it in found:
        print(it)