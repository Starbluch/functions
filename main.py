

def display_even_numbers():

    start=int(input("enter the first number:  "))
    finish=int(input("enter the second number:  "))
    if(start > finish):
        start, finish = finish, start

    for number in range(start, finish + 1):
        if (number % 2 == 0):
            print(number)


display_even_numbers()