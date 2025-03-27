import sys


def count_characters(text):
    """
    Count the number of upper letters, lower letters,
    punctuation marks, spaces and digits in a text.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    print(f"The text contains {len(text)} characters:")
    print(f"{len([c for c in text if c.isupper()])} upper letters")
    print(f"{len([c for c in text if c.islower()])} lower letters")
    print(f"{len([c for c in text if c in punctuation])} \
punctuation marks")
    print(f"{len([c for c in text if c.isspace()])} spaces")
    print(f"{len([c for c in text if c.isdigit()])} digits")


def main():
    """
    Main function to count characters in a text.
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit()

    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count? ")
        else:
            text = sys.argv[1]
    except EOFError:
        pass

    count_characters(text)


if __name__ == "__main__":
    main()
