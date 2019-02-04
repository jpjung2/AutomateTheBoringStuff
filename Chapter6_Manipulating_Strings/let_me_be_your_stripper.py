if __name__ == '__main__':
    text = '   Let me be your stripper, taking off lacquer no one does it quicker   '
    print(text, len(text))
    stripped = text.strip()

    print(stripped, len(stripped))

    stripped = text.rstrip()
    print(stripped, len(stripped))

    stripped = text.lstrip()
    print(stripped, len(stripped))

    stripped = text.strip(' ')
    print(stripped, len(stripped))
