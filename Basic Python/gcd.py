def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("GCD is:",gcd(a,b))