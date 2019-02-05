import pyperclip

def copy_pasta():
    msg = input("Enter some text and I'll copy it to your clipboard:")
    pyperclip.copy(msg)
    print(msg)

if __name__ == '__main__':
    copy_pasta()