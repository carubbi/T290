import sys

from strings import compress
from strings import expand

def main():
    """Sample client that calss compress() if the command-line argument is "-",
    and expand() if it is "+"."""
    if sys.argv[1] == "-":
        compress()
    elif sys.argv[1] == "+":
        expand()
    else:
        raise ValueError("Illegal command line argument")


if __name__ == "__main__":
    main()