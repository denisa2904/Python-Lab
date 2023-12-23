import sys
import os


def count_files(directory):

    extension_freq = {}
    for file in os.listdir(directory):
        try:
            extension = file.split(".")[1]
            if extension in extension_freq:
                extension_freq[extension] += 1
            else:
                extension_freq[extension] = 1
        except IndexError:
            continue
        except IOError:
            print("File access error")
            sys.exit(1)

    return extension_freq


def main():
    if len(sys.argv) != 2:
        try:
            raise ValueError
        except ValueError:
            print("Write: python ex4.py <directory>")
            sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        try:
            raise ValueError
        except ValueError:
            print("Invalid directory")
            sys.exit(1)

    if not os.listdir(directory):
        try:
            raise ValueError
        except ValueError:
            print("Directory is empty")
            sys.exit(1)

    extension_freq = count_files(directory)
    for extension in extension_freq:
        print(extension + ": " + str(extension_freq[extension]))


if __name__ == "__main__":
    main()
    