def intersection(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                print(a[i], end=" ")
    print()


def reunion(a, b):
    for i in range(len(a)):
        print(a[i], end=" ")
    difference(b, a)
    print()


def difference(a, b):
    for i in range(len(a)):
        ok = True
        for j in range(len(b)):
            if a[i] == b[j]:
                ok = False
        if ok:
            print(a[i], end=" ")
    print()


def main():
    a = input("List a: ").split()
    b = input("List b: ").split()
    print("a intersected with b: ", end="")
    intersection(a, b)
    print("a reunited with b: ", end="")
    reunion(a, b)
    print("a-b: ", end="")
    difference(a, b)
    print("b-a: ", end="")
    difference(b, a)


if __name__ == '__main__':
    main()

