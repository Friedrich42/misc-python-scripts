import math

def num_to_arr_by_its_digits(b):
    x = []
    b = str(b)
    for j in range(0, len(b)):
        x += [int(b[j])]
    return x

results = []
f = open('result_of_ideal_digit_invariants.txt', 'w')

for num in range(1, 10**20):
    num_arr = num_to_arr_by_its_digits(num)
    sum_of_powers_of_digit = 0
    for i in range(0, len(num_arr)):
        if(num_arr[i] == 0):
            continue
        sum_of_powers_of_digit += num_arr[i] ** num_arr[i]
    if(sum_of_powers_of_digit == num):
        results.append(num)
        print(str(num) + ' OK')
        f.write(str(num) + ' OK\n')
    else:
        print(str(num) + ' NOPE')
        f.write(str(num) + ' NOPE\n')

print(results)
f.write(str(results) + "\n")
f.close()
