"""Finding duplicate letters in a word."""

__author__ = "730407263"


def main() -> None:
    """Main function for repeat characters!"""
    word: str = str(input("Enter a word: "))
    print(repeats(word))


def repeats(word: str) -> bool:
    for i in word:
        if word.count(i) > 1:
            return True
        else:
            return False


if __name__ == '__main__':
    main()