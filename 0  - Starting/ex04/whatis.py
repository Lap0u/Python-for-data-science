import sys


def check_odd_or_even(number):
    if number % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            sys.exit(1)
        assert len(sys.argv) == 2, "more than one argument is provided"
        assert (
            sys.argv[1].startswith("-")
            and sys.argv[1][1:].isdigit()
            or sys.argv[1].isdigit()
        ), "argument is not an integer"
        number = int(sys.argv[1])
        check_odd_or_even(number)
    except (IndexError, ValueError):
        sys.exit(1)
