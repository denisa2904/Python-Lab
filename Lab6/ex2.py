import sys
import os


def rename(directory):

    i = 1
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            continue
        try:
            name = file.split(".")[0]
            extension = file.split(".")[1]
            os.rename(os.path.join(directory, file), os.path.join(directory, name + str(i) + "." + extension))
            i += 1
        except IOError:
            print("File can't be renamed")
            sys.exit(1)


def main():
    if len(sys.argv) != 2:
        try:
            raise ValueError
        except ValueError:
            print("Write: python ex2.py <directory>")
            sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        try:
            raise ValueError
        except ValueError:
            print("Invalid directory")
            sys.exit(1)

    rename(directory)


if __name__ == "__main__":
    main()
