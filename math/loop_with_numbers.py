'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
'''

def num_to_arr_by_its_digits(b):
    x = []
    b = str(b)
    for j in range(0, len(b)):
        x += [int(b[j])]
    return x

def persistence(n):
    n = num_to_arr_by_its_digits(n)
    flag = True
    steps = 1
    while(flag):
        if len(n) == 1:
            return 0
        num = 1
        for i in n:
            num *= i
        if len(str(num)) == 1:
            return steps
        else:
            n = num_to_arr_by_its_digits(num)
            steps += 1

print(str(persistence(39)) + " 3")
print(str(persistence(4)) + " 0")
print(str(persistence(25)) + " 2")
print(str(persistence(999)) + " 4")
