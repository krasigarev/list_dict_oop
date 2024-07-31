# ascii table

def compare_values(value_1, value_2):
    if value_1 < value_2:
        return value_2
    return value_1


if __name__ == "__main__":
    value_type = input()
    value_1 = input()
    value_2 = input()

    print(compare_values(value_1, value_2))
