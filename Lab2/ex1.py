def fibo(n):
    list = []
    a, b = 0, 1
    while a < n:
        list.append(a)
        c = a
        a = b
        b = c + b
    return list


# def main():
#     n = int(input("Enter a number: "))
#     print(fibo(n))
#
#
# main()
