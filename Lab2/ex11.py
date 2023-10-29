def order_list_of_tuples(string_tuples):
    result = string_tuples
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i][1][2] < result[j][1][2]:
                result[i], result[j] = result[j], result[i]
    return result


# SAU
# def order_list_of_tuples(string_tuples):
#     return sorted(string_tuples, key=lambda x: x[1][2])


def main():
    string_tuples = [("random", "aac"), ("nu", "aad"), ("conteaza", "aab")]
    print(order_list_of_tuples(string_tuples))


if __name__ == '__main__':
    main()
