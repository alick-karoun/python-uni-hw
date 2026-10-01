def convert(text):
    return text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


def main():
    text = input("Text: ")
    print(convert(text))


main()