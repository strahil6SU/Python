def sumVowelsDigits():
    input_word = input("Въведи дума: ")
    sum = 0

    for i in range (0, len(input_word)):
        if input_word[i] == 'a':
            sum += 1
        elif input_word[i] == 'e':
            sum += 2
        elif input_word[i] == 'i':
            sum += 3
        elif input_word[i] == 'o':
            sum += 4
        elif input_word[i] == 'u':
            sum += 5
    print("The sum on vowels = ", sum)
sumVowelsDigits()