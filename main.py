

def print_square (symbol, size, boLL):
    if boLL == True:
        for i in range (size):
            print((symbol + '  ') * size)
    elif boLL == False:
        for i in range (size):
            if (i == 0 or i == size - 1):
                print(symbol * size )
            else:
                print(symbol + ' ' * (size - 2) + symbol)
    else:
        print('Invalid variation, try again')


size = int(input("Enter square size: "))
symbol = input("Enter symbol: ")
boLL = input("Enter True or False: ").strip().lower() == 'true'


print_square(symbol, size, boLL)