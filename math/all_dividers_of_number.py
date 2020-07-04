number = int(input("Enter a number to know all its dividers\n"))
dividers = []

for i in range(1, number):
    if not (number % i):
        dividers.append(i)

print(dividers)
