import sys


def is_punct(char):
    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count_char(text):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    punctuation_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif is_punct(char):
            punctuation_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    total_characters = len(text)
    print(f"The text contains {total_characters} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    s_arg = ""

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) < 2 or sys.argv is None:
            s_arg = input("What is the text to count?\n")
            s_arg += "\n"
        else:
            s_arg = sys.argv[1]
        count_char(s_arg)
    except AssertionError as e:
        print("Assertion Error: ", e)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
