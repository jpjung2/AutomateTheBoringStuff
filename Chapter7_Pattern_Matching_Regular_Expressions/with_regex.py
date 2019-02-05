import re

def isPhoneNumber(text):
    pregex = re.compile(r'\d{3}-\d{3}-\d{4}')

    result = pregex.search(text)
    if result is None:
        return False
    print(result.group())
    return True


if __name__ == '__main__':

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    if isPhoneNumber(message):
        print("Number found:", message)

    new_message = "Tacos"
    if isPhoneNumber(new_message):
        print("Number found:", new_message)

