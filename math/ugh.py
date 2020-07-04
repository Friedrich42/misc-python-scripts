def is_my_digit_in_number(n, d):
    p = 1
    while(n):
        digit = n % 10
        if(digit == d):
            return True
            break
        n//=10
        p+=1
    return False

start_range = int(input("Enter start of range"))
stop_range = int(input("Enter stop of range"))
wanted_digit = int(input("Enter wanted digit"))

counter = 0

for i in range(start_range, stop_range):
    if(is_my_digit_in_number(i, wanted_digit)):
        counter+=1

print(counter)

# start_range = int(input("Enter start of range\n"))
# stop_range = int(input("Enter stop of range\n"))
# wanted_digit = int(input("Enter wanted digit\n"))
#
# counter = 0
#
# for i in range(start_range, stop_range):
#     if(str(wanted_digit) in str(i)):
#         counter+=1
#
# print(counter)