import sys


def main() -> None:
    argc = len(sys.argv)
    program_name = sys.argv[0]

    print(f"Program name: {program_name}")
    if argc < 2:
        print("No arguments provided!")
        print(f"Total arguments: {argc}")
        return

    print(f"Arguments received: {argc - 1}")
    count = 0
    for arg in sys.argv[1:]:
        count += 1
        print(f"Argument {count}: {arg}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
