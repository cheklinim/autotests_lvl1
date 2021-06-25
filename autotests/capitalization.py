def main():
    print("Hello to Capitalization!")


def capitalization(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


if __name__ == "__main__":
    main()

