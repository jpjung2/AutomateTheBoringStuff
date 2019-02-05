def isPhoneNumber(num):
    if len(num) != 12:
        return False
    if num[3] != '-' or num[7] != '-':
        return False

    return num[:3].isnumeric() and num[4:7].isnumeric() and num[-4:].isnumeric()


if __name__ == '__main__':
    print("No regular expressions to see here")
    pn = input("Give me a phone number in the form of XXX-XXX-XXXX: ")
    if isPhoneNumber(pn):
        print("Yay!", pn, "is a valid phone number")
    else:
        print("Invalid number", pn)
