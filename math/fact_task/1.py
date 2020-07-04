import math

all_digits = []

for x in range(1, 10**7):
    x_copy  = x
    x_copy1 = x
    x_digits = []

    while x > 0: # тут переводим число в массив, состоящий из его цифр
      x_digits.append(x % 10)
      x = x // 10
    x_digits = x_digits[::-1]

    for i in range(0, len(x_digits)): # подчиняется ли число алгоритму
        x_copy-=math.factorial(x_digits[i])

    if(x_copy == 0):
        all_digits.append(x_copy1)

print(all_digits)
