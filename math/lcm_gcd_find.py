def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

try:
    a = int(input("Enter first value\n"))
    b = int(input("Enter second value\n"))
except Exception as e:
    print("Exception raised")

gcd_val = int(gcd(a, b))
lcm_val = int(lcm(a, b))
print( "LCM of these values is " + str(lcm_val) + "\nGCD of these values is " + str(gcd_val))
