def sumNumber():
    input_number = input("Въведи число: ")
    sum = 0

    for i in range(0, len(input_number)):
        sum += int(input_number[i])
    print("The digits sum = ", sum)

sumNumber()