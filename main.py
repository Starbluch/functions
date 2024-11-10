def find_min(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    Min = numbers[0]

    for num in numbers:
        if (num < Min):
            Min = num

    return Min

result = find_min(20, 34,9, 15, 6)
print("Minimum number: ", result)


def find_max(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    Max = numbers[0]

    for num in numbers:
        if (num > Max):
            Max = num

    return Max


result = find_max(20, 34,9, 15, 6)
print("Maximum number: ", result)
