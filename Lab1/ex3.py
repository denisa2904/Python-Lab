def string_occurrence(small_string, big_string):
    count = 0
    for i in range(len(big_string)):
        if big_string[i:i + len(small_string)] == small_string:
            count += 1
    return count


def main():
    small_string = input("Enter the first string: ")
    big_string = input("Enter the second string: ")
    print(string_occurrence(small_string, big_string))
    # print(string_occurrence("ab", "abcabcabc"))


main()
