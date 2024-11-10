def is_palindrome():
    num = str(input("Enter a number: "))

    count = 0
    for chet in num:
        count += 1
    for i in range(count // 2):
        if (num[i] != num[count - 1 - i]):
            print("Oh noooo better luck next time")
            return False

    print("Ehyyy, this is a palindrome!")


is_palindrome()