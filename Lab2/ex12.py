def rhyming(words):
    result = []
    checked = []
    for i in range(len(words)):
        res = []
        if words[i] not in checked:
            for j in range(i, len(words)):
                if words[i][-2:] == words[j][-2:] and words[j] not in checked:
                    res.append(words[j])
                    checked.append(words[j])
            if res:
                result.append(res)
    return result


def main():
    words = ['ana', 'banana', 'carte', 'parte', 'arme']
    print(rhyming(words))


if __name__ == '__main__':
    main()
