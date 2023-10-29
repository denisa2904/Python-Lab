import ex2


def compare_dict(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key not in dict2:
            return False
        if type(dict1[key]) != type(dict2[key]):
            return False
        if type(dict1[key]) == dict:
            if not compare_dict(dict1[key], dict2[key]):
                return False
        else:
            if dict1[key] != dict2[key]:
                return False
    return True


def main():
    dict1 = ex2.count_char('Ana has apples.')
    dict2 = ex2.count_char('Ana has apples.')
    print(compare_dict(dict1, dict2))

    dict1 = ex2.count_char('Ana has apples.')
    dict2 = ex2.count_char('Ana eats apples.')
    print(compare_dict(dict1, dict2))

    dict1 = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
    dict2 = {'a': 1, 'b': 2, 'c': [1, 2]}
    print(compare_dict(dict1, dict2))


if __name__ == '__main__':
    main()
