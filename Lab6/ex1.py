import sys
import os


def print_dir(directory=".", extension=".txt"):

    if not os.path.isdir(directory):
        print("Invalid directory")
        sys.exit(1)

    for file in os.listdir(directory):
        if file.endswith(extension):
            try:
                with open(os.path.join(directory, file), "r") as f:
                    print(f.read())
            except IOError:
                print("File access error")
                sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Write: python ex1.py <directory> <extension>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]
    print_dir(directory, extension)


if __name__ == "__main__":
    main()
