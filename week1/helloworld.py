import sys


def main():
    if len(sys.argv) != 2:
        print("Please include your name")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
