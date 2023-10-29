def validate_dict(s, d):
    for key in d:
        is_key = False
        for rule in s:
            if rule[0] == key:
                is_key = True
                if not d[key].startswith(rule[1]):
                    return False
                if not d[key].endswith(rule[3]):
                    return False
                if d[key].startswith(rule[2]) or d[key].endswith(rule[2]) or rule[2] not in d[key]:
                    return False
        if not is_key:
            return False
    return True


def main():
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d1 = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    d2 = {"key1": "come inside, it's cold", "key2": "start studying in the middle of winter"}
    d3 ={"key2": "start in the winter"}
    print(validate_dict(s, d1))
    print(validate_dict(s, d2))
    print(validate_dict(s, d3))


if __name__ == '__main__':
    main()