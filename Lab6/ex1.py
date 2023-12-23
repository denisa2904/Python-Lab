import sys
import os


def print_dir(directory, extension):

    for file in os.listdir(directory):
        if file.split(".")[1] == extension[1:]:
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
    if not os.path.isdir(directory):
        try:
            raise ValueError
        except ValueError:
            print("Invalid directory")
            sys.exit(1)

    extension = sys.argv[2]
    if not extension.startswith("."):
        try:
            raise ValueError
        except ValueError:
            print("Invalid extension")
            sys.exit(1)

    print_dir(directory, extension)


if __name__ == "__main__":
    main()
