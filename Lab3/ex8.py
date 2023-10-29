def get_path(mapping):
    values = []
    current_key = "start"
    while current_key not in values:
        values.append(current_key)
        current_key = mapping[current_key]
    return values


def main():
    print(get_path({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
# loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
# will return ['a', '6', 'z', '2']


if __name__ == '__main__':
    main()
