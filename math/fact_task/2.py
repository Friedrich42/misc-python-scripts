import math

result = []

for b in range(1, 10**5):
    b_cp = b
    x = []
    s = str(b)
    for j in range(0, len(s)):
        x += [int(s[j])]
        b -= math.factorial(x[j])
    if(b == 0):
        result.append(b_cp)

print(result)
