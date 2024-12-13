def numbeDivideNine():
    start_number = int(input("Начално число: "))
    end_number = int(input("Крайно число: "))

    sum = 0

    for index in range(start_number, end_number+1):
        if index % 9 == 0:
            sum += index
            print(index)

    print("The sum = ", sum)

numbeDivideNine()