array_of_numbers = []
array_of_results = []

for i in range(0, 6):
    array_of_numbers.append(int(input(f"Введите {i+1} число \n")))
    if(array_of_numbers[i] < 0):
        array_of_results.append("Отрицательный элемент")
    elif(array_of_numbers[i] == 0):
        array_of_results.append("Это ноль")
    else:
        array_of_results.append("Положительный элемент")

print(array_of_results)
