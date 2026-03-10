import argparse


def main():
    parser = argparse.ArgumentParser(description="Sum integers.")

    parser.add_argument("numbers", nargs="*", type=int,
                        help="Integers to sum")

    parser.add_argument("-f", "--file", type=str,
                        help="Path to input file")

    parser.add_argument("-o", "--output", type=str,
                        help="Path to output file")

    args = parser.parse_args()

    total = 0

    if args.file:
        try:
            with open(args.file, "r") as f:
                for line in f:
                    try:
                        total += int(line.strip())
                    except ValueError:
                        print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")
        except FileNotFoundError as e:
            print("Error reading file:", e)
            return

    else:
        total = sum(args.numbers)

    if args.output:
        with open(args.output, "w") as f:
            f.write(str(total))  
    else:
        print(total)


if __name__ == "__main__":
    main()