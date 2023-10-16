def convert_string(old_string):
    new_string = ""
    for i in old_string:
        if i.isupper():
            if len(new_string) == 0:
                new_string += i.lower()
            elif new_string[len(new_string)-1].islower():
                new_string += "_" + i.lower()
        else:
            new_string += i
    return new_string


def main():
    old_string = input("Enter a string: ")
    print(convert_string(old_string))


if __name__ == '__main__':
    main()