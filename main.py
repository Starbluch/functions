def count_digits():
    number = int(input("Enter a number: "))
    count = 0

    if number < 0:
        number = -number

    if (number == 0):
        return 1

    while number > 0:
        number //= 10
        count += 1
    print(count)



count_digits()