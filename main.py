
def product_of_range():
    start = int(input("Enter the first number: "))
    fin = int(input("Enter the second number: "))


    if (start == fin):
        print(start)
    else:

        if (start > fin):
            start, fin = fin, start

        result = 1
        for number in range(start, fin + 1):
            result *= number
        return result


print(product_of_range())