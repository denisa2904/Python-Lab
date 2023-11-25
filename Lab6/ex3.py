import sys
import os


def total_size(directory):
    if not os.path.isdir(directory):
        print("Invalid directory")
        sys.exit(1)

    size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                size += os.path.getsize(os.path.join(root, file))
            except IOError:
                print("File access error")
                sys.exit(1)

    return str(size) + " bytes"


def main():
    if len(sys.argv) != 2:
        print("Write: python ex3.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    print(total_size(directory))


if __name__ == "__main__":
    main()
