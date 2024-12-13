def multiplicationTable():
    input_number = int(input("Въведете число между 1 и 10: "))
    multiplication = 0

    for i in range(1, 11):
        multiplication = i * input_number
        print(f'{i} * {input_number} = {multiplication}')

multiplicationTable()