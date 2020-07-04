#Условие задачи: найдите трехзначное число, сумма цифр которого == 20, а сумма квадратов делится на 3, но не делится на 9
for i in range(100,999):
    first_digit = int(i / 100)
    second_digit = int((i % 100) / 10)
    third_digit = (i % 100) % 10
    summ_of_digits = first_digit + second_digit + third_digit
    summ_of_squares = (first_digit**2) + (second_digit**2) + (third_digit**2)

    if(summ_of_digits == 20 and summ_of_squares % 3 == 0 and summ_of_squares % 9 != 0):
        print(int(i))
        break
