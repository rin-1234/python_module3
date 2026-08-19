import sys

def main():
    argc = len(sys.argv)
    program_name = sys.argv[0]

    print(f"Program name: {program_name}")
    if argc < 2:
        print("No arguments provided!")
        print(f"Total arguments: {argc}")
        return

    print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()