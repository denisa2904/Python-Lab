def most_common_letter(phrase):
    letter_counts = {}
    max_count = 0
    max_letter = None
    for character in phrase:
        if character.isupper():
            letter = character.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
                if letter_counts[letter] > max_count:
                    max_count = letter_counts[letter]
                    max_letter = letter
            else:
                letter_counts[letter] = 1
    return max_letter


def main():
    phrase = input("Enter a phrase: ")
    print(most_common_letter(phrase))


main()
