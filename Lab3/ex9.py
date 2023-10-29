def my_function(*pos_args, **kw_args):
    count = 0
    for arg in pos_args:
        if arg in kw_args.values():
            count += 1
    return count


def main():
    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == '__main__':
    main()
