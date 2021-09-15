"""An exercise in remainders and boolean logic."""

__author__ = "730407263"


# Begin your solution here...


def main() -> None:
    """The Tar Heel Exercise."""
    num: int = int(input("Enter an int: "))
    print(tar_heels(num))


def tar_heels(num: int) -> str:
    if num % 2 == 0 and num % 7 == 0:
        return ("TAR HEELS")
    else:
        if num % 2 == 0:
            return ("TAR")
        else:
            if num % 7 == 0:
                return ("HEELS")
            else:
                return ("CAROLINA")


if __name__ == "__main__":
    main()