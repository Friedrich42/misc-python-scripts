"""
Разбейте целое число на цифры, пары цифр, тройки цифр и т.д. по написанию и выведите рядом с ними True, если они простые, False если нет
"""

def num_to_arr_by_its_digits(b):
    x = []
    b = str(b)
    for j in range(0, len(b)):
        x += [int(b[j])]
    return x


def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True


number = 0
try:
    number = int(input("Enter digit\n"))
except Exception as e:
    print(e)

number_by_digits = num_to_arr_by_its_digits(number)
number_by_digits_str = list([str(n) for n in number_by_digits])
i = 0
while i < len(number_by_digits):
    length = i + 1
    while length <= len(number_by_digits):
        n = int("".join(number_by_digits_str[i:length]))
        print(f"{n} {test_prime(n)}")
        length += 1
    i += 1
